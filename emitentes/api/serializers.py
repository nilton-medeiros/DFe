from rest_framework import serializers
from emitentes import models


class EmitenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Emitente
        fields = (
            'id',
            'nome',
            'cnpj',
            'inscricao_estadual',
            'cpf',
            'logradouro',
            'numero',
            'complemento',
            'bairro',
            'municipio',
            'uf',
            'cep',
            'telefones',
            'email',
            'logotipo_dfe',
        )


class NFeEmiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Emitente
        fields = (
            'id',
            'nfe_serie',
            'nfe_numero',
            'nfe_serie_homologacao',
            'nfe_numero_homologacao',
        )


class NFCeEmiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Emitente
        fields = (
            'id',
            'nfce_serie',
            'nfce_numero',
            'nfce_serie_homologacao',
            'nfce_numero_homologacao',
        )


class CTeEmiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Emitente
        fields = (
            'id',
            'cte_serie',
            'cte_numero',
            'cte_serie_homologacao',
            'cte_numero_homologacao',
        )


class MDFeEmiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Emitente
        fields = (
            'id',
            'mdfe_serie',
            'mdfe_numero',
            'mdfe_serie_homologacao',
            'mdfe_numero_homologacao',
        )
