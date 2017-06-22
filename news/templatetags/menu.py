from django import template
from ..models import Category, Page

register = template.Library()

@register.inclusion_tag('menu.html')
def show_menu(menu):
    categories = Category.objects.all()
    pages = Page.objects.all()
    return {'categories': categories, 'pages': pages}
