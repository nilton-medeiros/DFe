from django.contrib import admin
from .models import Emitente


class EmitenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'cpf', 'municipio', 'uf', 'telefones', 'email', 'emissoes_ativo', 'cadastro_ativo')

admin.site.register(Emitente, EmitenteAdmin)
