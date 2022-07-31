from django.contrib import admin

from .models import Categoria, Post

# Register your models here.


class CategoriaAdmin(admin.ModelAdmin):
   readonly_fields=('created','update')

class PostaAdmin(admin.ModelAdmin):
   readonly_fields=('created','update')



admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Post,PostaAdmin)