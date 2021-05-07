from django.contrib import admin
from .models import Emitente


class EmitenteAdmin(admin.ModelAdmin):
    list_display = ('nome',
                    'cnpj',
                    'cpf',
                    'municipio',
                    'uf',
                    'telefones',
                    'email',
                    'emissoes_suspensas',
                    'is_active',
                    'created_at',
                    'updated_at')


admin.site.register(Emitente, EmitenteAdmin)
