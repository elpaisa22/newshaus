#from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
from django.db.models import Count
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import PostForm
from .models import *
from layout.models import Block
import itertools

class TemplateIterator(itertools.count):
    def next_number(self):
        return next(self)

# Create your views here.
def default_view(request):
        iterator=TemplateIterator()
        posts = Post.objects.annotate(Count('pk')).order_by('-publish_date')[:10]
        blocks = Block.objects.all()
        return render(request, 'default.html', {'blocks' : blocks, 'posts': posts, 'iterator':iterator})

def post_by_category(request, category_name):
        category = get_object_or_404(Category, name=category_name)
        posts = Post.objects.filter(category__name=category_name, publish_date__lte=timezone.now()).order_by('-publish_date')
        advertisings = Advertising.objects.all().order_by('?')[:4]
        page = request.GET.get('page', 1)

        paginator = Paginator(posts, 10)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        if (int(page) > 1):
            return render(request, 'article/article_list_others.html', {'posts': posts, 'category': category, 'advertisings' : advertisings})
        else:
            return render(request, 'article/article_list.html', {'posts': posts, 'category': category, 'advertisings' : advertisings})


def post_detail(request, slug, pk):
        post = get_object_or_404(Post, pk=pk)
        advertisings = Advertising.objects.all().order_by('?')[:4]
        return render(request, 'article/article_detail.html', {'post': post, 'advertisings' : advertisings})

def search_text(request):
        query = request.GET.get('q')

        advertisings = Advertising.objects.all().order_by('?')[:4]

        if query:
            posts = Post.objects.filter(text__contains=query).order_by('-publish_date');
            page = request.GET.get('page', 1)

            paginator = Paginator(posts, 10)
            try:
                posts = paginator.page(page)
            except PageNotAnInteger:
                posts = paginator.page(1)
            except EmptyPage:
                posts = paginator.page(paginator.num_pages)
            return render(request, 'article/search_result.html', {'query': query, 'posts': posts, 'advertisings' : advertisings})
        else:
            return render(request, 'article/search_result.html', {'query': query, 'advertisings' : advertisings})

def generic_page_view(request, page_name):
    page = get_object_or_404(Page, name=page_name)
    return render(request, 'generic_page.html', {'page' : page})
