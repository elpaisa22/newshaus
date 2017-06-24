from django.db import models

# Create your models here.
class Block(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=100)
    order = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Bloque'
        verbose_name_plural = 'Bloques'
        ordering = ['order']

class Column(models.Model):
    order = models.PositiveIntegerField(verbose_name="Orden")
    width = models.PositiveIntegerField(verbose_name="Ancho")
    block = models.ForeignKey(Block, null=True, related_name='columns')

    def __str__(self):
        return self.block.name + ' - ' + str(self.order)

    class Meta:
        verbose_name = 'Columna'
        verbose_name_plural = 'Columnas'
        ordering = ['block__order', 'order']

class ContentElement(models.Model):
    CONTENT_TYPES = (
        ('ADV', 'Publicidad'),
        ('ART', 'Articulo Grande'),
        ('THU', 'Articulo Pequeño'),
        ('CAR', 'Carrusel'),
        ('CUS', 'Personalizado'),
    )
    order = models.PositiveIntegerField(verbose_name="Orden")
    column = models.ForeignKey(Column, null=True, related_name='elements')
    content_type = models.CharField(max_length=3, choices=CONTENT_TYPES,verbose_name="Tipo de Contenido")

    html_code = models.TextField(null = True, blank = True, verbose_name="Contenido Personalizado")
    advertising = models.ImageField(upload_to='images/advertising', null = True, blank = True, verbose_name="Imagen de Publicidad")

    def __str__(self):
        return self.column.block.name + ' - columna: ' + str(self.column.order) + ' - Tipo : ' + self.content_type + ' - Orden: ' + str(self.order)

    class Meta:
        verbose_name = 'Elemento'
        verbose_name_plural = 'Elementos'
        ordering = ['column__order','order']
