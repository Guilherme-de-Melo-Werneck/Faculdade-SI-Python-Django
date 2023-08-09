from django.contrib import admin
from.models import Pessoas
class PessoasAdmin (admin.ModelAdmin):
    list_display = ['nome', 'telefone', 'idade']
    search_fields = ['nome']
    list_filter = ['idade']
    list_editable = ['telefone', 'idade']

# Register your models here.
admin.site.register(Pessoas, PessoasAdmin)
