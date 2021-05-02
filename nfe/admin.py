from django.contrib import admin

from .models import Nfe


class NfeAdmin(admin.ModelAdmin):
    list_display = ('emitente_id', 'serie', 'numero', 'numero_carta_correcao', 'chave', 'data_emissao', 'situacao',
                    'status_sefaz')


admin.site.register(Nfe, NfeAdmin)
