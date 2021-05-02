from rest_framework import serializers

from emitentes import models, validators


class NFeEmiteSerializer(serializers.ModelSerializer):
    certificado_a1 = serializers.FileField(validators=[validators.validate_certificado_a1])
    logotipo_dfe = serializers.FileField(validators=[validators.validate_logotipo_dfe])

    class Meta:
        model = models.Emitente
        fields = (
            'id',
            'nfe_serie',
            'logotipo_dfe',
            'certificado_a1',
            'nfe_serie_homologacao',
            'nfe_numero_homologacao',
        )


class NFCeEmiteSerializer(serializers.ModelSerializer):
    certificado_a1 = serializers.FileField(validators=[validators.validate_certificado_a1])
    logotipo_dfe = serializers.FileField(validators=[validators.validate_logotipo_dfe])

    class Meta:
        model = models.Emitente
        fields = (
            'id',
            'nfce_serie',
            'logotipo_dfe',
            'certificado_a1',
            'nfce_serie_homologacao',
            'nfce_numero_homologacao',
        )


class CTeEmiteSerializer(serializers.ModelSerializer):
    certificado_a1 = serializers.FileField(validators=[validators.validate_certificado_a1])
    logotipo_dfe = serializers.FileField(validators=[validators.validate_logotipo_dfe])

    class Meta:
        model = models.Emitente
        fields = (
            'id',
            'cte_serie',
            'logotipo_dfe',
            'certificado_a1',
            'cte_serie_homologacao',
            'cte_numero_homologacao',
        )


class MDFeEmiteSerializer(serializers.ModelSerializer):
    certificado_a1 = serializers.FileField(validators=[validators.validate_certificado_a1])
    logotipo_dfe = serializers.FileField(validators=[validators.validate_logotipo_dfe])

    class Meta:
        model = models.Emitente
        fields = (
            'id',
            'mdfe_serie',
            'logotipo_dfe',
            'certificado_a1',
            'mdfe_serie_homologacao',
            'mdfe_numero_homologacao',
        )


class EmitenteSerializer(serializers.ModelSerializer):
    certificado_a1 = serializers.FileField(validators=[validators.validate_certificado_a1])
    logotipo_dfe = serializers.FileField(validators=[validators.validate_logotipo_dfe])

    class Meta:
        model = models.Emitente
        fields = (
            'id',
            'nome',
            'nfe_numero',
            'nfe_serie_homologacao',
            'certificado_a1',
            'logotipo_dfe'
        )

    def to_representation(self, instance):
        data = {
            'id': instance.id,
            'nome': instance.nome,
        }
        if instance.cnpj:
            data['cnpj'] = instance.cnpj
        else:
            data['cpf'] = instance.cpf

        for emit in 'nfe_emite nfce_emite cte_emite mdfe_emite'.split():
            base_name = emit.split('_')[0]
            if getattr(instance, emit):
                data[f'{base_name}_serie'] = getattr(instance, f'{base_name}_serie')
                data[f'{base_name}_numero'] = getattr(instance, f'{base_name}_numero')
                data[f'{base_name}_serie_homologacao'] = getattr(instance, f'{base_name}_serie_homologacao')
                data[f'{base_name}_numero_homologacao'] = getattr(instance, f'{base_name}_numero_homologacao')

        return data
