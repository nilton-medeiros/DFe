from rest_framework import serializers
from emitentes import models


class EmitenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Emitente
        tup1 = ('id', 'nome')

        if model.cnpj:
            tup2 = ('cnpj',)
        else:
            tup2 = ('cpf',)

        tup3 = ()
        tup4 = ()
        tup5 = ()
        tup6 = ()

        if model.nfe_emite:
            tup3 = ('nfe_serie', 'nfe_numero', 'nfe_serie_homologacao', 'nfe_numero_homologacao')
        if model.nfce_emite:
            tup4 = ('nfce_serie', 'nfce_numero', 'nfce_serie_homologacao', 'nfce_numero_homologacao')
        if model.cte_emite:
            tup5 = ('cte_serie', 'cte_numero', 'cte_serie_homologacao', 'cte_numero_homologacao')
        if model.mdfe_emite:
            tup6 = ('mdfe_serie', 'mdfe_numero', 'mdfe_serie_homologacao', 'mdfe_numero_homologacao')

        fields = tup1 + tup2 + tup3 + tup4 + tup5 + tup6

        # print(f'cnpj: {model.cnpj.field()}, \n nfe_emite: {model.nfe_emite.remote_field()}')
