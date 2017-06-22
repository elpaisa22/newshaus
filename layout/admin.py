from django.contrib import admin
from .models import *

# Register your models here.
class ColumnInline(admin.TabularInline):
    model = Column

class BlockAdmin(admin.ModelAdmin):
    inlines = [ColumnInline,]

class ContentElementInline(admin.TabularInline):
    model = ContentElement

class ColumnAdmin(admin.ModelAdmin):
    inlines = [ContentElementInline,]

admin.site.register(ContentElement)
admin.site.register(Column, ColumnAdmin)
admin.site.register(Block, BlockAdmin)
