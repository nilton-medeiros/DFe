from rest_framework import serializers


def validate_certificado_a1(value):
    if not value:
        raise serializers.ValidationError('Certificado A1 não pode estar vazio')
    return value


def validate_logotipo_dfe(value):
    if not value:
        raise serializers.ValidationError('Logo Tipo não pode estar vazio')
    return value
