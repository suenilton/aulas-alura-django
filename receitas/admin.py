from django.contrib import admin
from .models import Receita


class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita','categoria','tempo_preparo','get_date_formated', 'status_receita')
    list_display_links = ('id','nome_receita')
    search_fields = ('nome_receita',)
    list_filter = ('categoria','tempo_preparo', 'status_receita')
    list_editable = ('status_receita',)
    list_per_page = 10
    
    def get_date_formated(self, obj):
        if obj.date_receita:
            return obj.date_receita.strftime('%d/%m/%Y')
    
    get_date_formated.short_description = 'data de publicação'



admin.site.register(Receita, ListandoReceitas)