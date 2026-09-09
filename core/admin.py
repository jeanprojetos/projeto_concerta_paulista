from django.contrib import admin
from .models import Denuncia

@admin.register(Denuncia)
class DenunciaAdmin(admin.ModelAdmin):
    list_display = ('rua', 'bairro', 'status', 'data_criacao')
    list_editable = ('status',)
    list_filter = ('status', 'bairro')