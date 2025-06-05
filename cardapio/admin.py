from django.contrib import admin

# Register your models here.

from . models import Cardapio

class CarAdmin(admin.ModelAdmin):
    readonly_fields=["adicionado","editado"]

admin.site.register(Cardapio,CarAdmin)