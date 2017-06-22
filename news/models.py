from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name  = models.CharField(max_length=20, verbose_name="Nombre")
    description = models.CharField(max_length=200, verbose_name="Descripción")

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

class Post(models.Model):
    author = models.ForeignKey('auth.User', null=True, verbose_name="Autor")
    title  = models.CharField(max_length=400, verbose_name="Titulo")
    subtitle  = models.CharField(max_length=400, null=True, verbose_name="Sub Titulo")
    text   = models.TextField(verbose_name="Texto")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Creado")
    publish_date = models.DateTimeField(default=timezone.now, verbose_name="Publicado")
    category = models.ForeignKey(Category, null=True, related_name='posts', verbose_name="Categoría")

    def slug(self):
        return slugify(self.title)

    def defaultImage(self):
        return self.images.first()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'

class Image(models.Model):
    name = models.TextField(verbose_name="Nombre")
    image = models.ImageField(upload_to='images', null = True, blank = True)
    post = models.ForeignKey(Post, null=True, related_name='images')

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imágenes'

class Page(models.Model):
    visible_name = models.CharField(verbose_name="Nombre Visible", max_length=100)
    name = models.CharField(verbose_name="Nombre", max_length=100)
    text = models.TextField(verbose_name="Texto")

    def __str__(self):
        return self.visible_name

    class Meta:
        verbose_name = 'Página'
        verbose_name_plural = 'Paginas'

class Advertising(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=100)
    order = models.PositiveIntegerField(verbose_name="Orden")
    image = models.ImageField(upload_to='images/advertising')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Publicidad'
        verbose_name_plural = 'Publicidades'
