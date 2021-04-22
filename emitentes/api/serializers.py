from rest_framework import serializers
from emitentes import models


class EmitenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Emitente
        fields = ('id', 'nome')

        # if model.nfe_emite:
        #     tup3 = ('nfe_serie', 'nfe_numero', 'nfe_serie_homologacao', 'nfe_numero_homologacao')
        # if model.nfce_emite:
        #     tup4 = ('nfce_serie', 'nfce_numero', 'nfce_serie_homologacao', 'nfce_numero_homologacao')
        # if model.cte_emite:
        #     tup5 = ('cte_serie', 'cte_numero', 'cte_serie_homologacao', 'cte_numero_homologacao')
        # if model.mdfe_emite:
        #     tup6 = ('mdfe_serie', 'mdfe_numero', 'mdfe_serie_homologacao', 'mdfe_numero_homologacao')

    def to_representation(self, instance):
        data = {
            'id': instance.id,
            'nome': instance.nome,
        }

        if instance.cnpj:
            data['cnpj'] = instance.cnpj
        else:
            data['cpf'] = instance.cpf

        if instance.nfe_emite:
            data['nfe_serie'] = instance.nfe_serie

        return data
