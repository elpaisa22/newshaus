from django.contrib import admin
from django.forms import ModelForm
from suit_redactor.widgets import RedactorWidget
from django import forms
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Advertising)

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('image', 'post')

class PostForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'style':'width:80%'}))
    subtitle = forms.CharField(widget=forms.TextInput(attrs={'style':'width:80%'}))

    class Meta:
        widgets = {
            'text': RedactorWidget(editor_options={'lang': 'es'})
        }

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostForm

    list_display = (
        'title',
        'created_date',
        'publish_date',
        'author',
    )

    fieldsets = (
        (None, {
            'fields': ['author',
                       'title',
                       'subtitle',
                       'text',
                       'category',
                       'created_date',
                       'publish_date',
                       '_picture_view'],
        }),
    )

    inlines = [ ImageInline, ]

    readonly_fields = (
        '_picture_view',
    )

    def _picture_view(self, obj):
        html=''
        images = Image.objects.filter(post=obj)
        if len(images) == 0:
            return ''
        for img in images:
            html += '<img src="{}" class="col-xs-4 col-md-2" style="max-height:200px;"/>'.format(img.image.url)
        return html
    _picture_view.short_description = 'Vista previa'
    _picture_view.allow_tags = True

class PageForm(ModelForm):
    class Meta:
        widgets = {
            'text': RedactorWidget(editor_options={'lang': 'es'})
        }

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    form = PageForm
