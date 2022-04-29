from django.contrib import admin
from .models import Pessoa

class ModelPessoas(admin.ModelAdmin):
    list_display = ('id', 'nome_pessoa', 'email_pessoa')
    list_display_links = ('id', 'nome_pessoa')
    search_fields = ('nome_pessoa',)



admin.site.register(Pessoa, ModelPessoas)