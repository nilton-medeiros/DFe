from rest_framework import serializers

from nfe.models import Nfe


class NfeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nfe
        fields = '__all__'
