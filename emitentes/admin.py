from django.contrib import admin
from .models import Emitente


class EmitenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'token', 'cnpj', 'cpf', 'municipio', 'uf', 'telefones', 'email', 'emissoes_status',
                    'emitente_status')


admin.site.register(Emitente, EmitenteAdmin)
