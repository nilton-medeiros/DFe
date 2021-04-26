from rest_framework import serializers
from emitentes import models


class EmitenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Emitente
        fields = ('id', 'nome', 'certificado_a1', 'logotipo_dfe')

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
            data['nfe_numero'] = instance.nfe_numero
            data['nfe_serie_homologacao'] = instance.nfe_serie_homologacao
            data['nfe_numero_homologacao'] = instance.nfe_numero_homologacao

        if instance.nfce_emite:
            data['nfce_serie'] = instance.nfce_serie
            data['nfce_numero'] = instance.nfce_numero
            data['nfce_serie_homologacao'] = instance.nfce_serie_homologacao
            data['nfce_numero_homologacao'] = instance.nfce_numero_homologacao

        if instance.cte_emite:
            data['cte_serie'] = instance.cte_serie
            data['cte_numero'] = instance.cte_numero
            data['cte_serie_homologacao'] = instance.cte_serie_homologacao
            data['cte_numero_homologacao'] = instance.cte_numero_homologacao

        if instance.mdfe_emite:
            data['mdfe_serie'] = instance.mdfe_serie
            data['mdfe_numero'] = instance.mdfe_numero
            data['mdfe_serie_homologacao'] = instance.mdfe_serie_homologacao
            data['mdfe_numero_homologacao'] = instance.mdfe_numero_homologacao

        data['certificado_a1'] = instance.certificado_a1
        data['logotipo_dfe'] = instance.logotipo_dfe

        return data
