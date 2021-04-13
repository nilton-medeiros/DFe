from django.db import models


class Emitente(models.Model):
    nome = models.CharField('Nome', max_length=60)
    cnpj = models.CharField('CNPJ', max_length=14, null=True)
    inscricao_estadual = models.CharField('Inscrição Estadual', max_length=14, null=True, blank=True)
    cpf = models.CharField('CPF', max_length=11, null=True, blank=True)
    logradouro = models.CharField(max_length=60)
    numero = models.CharField(max_length=40)
    complemento = models.CharField(max_length=60, null=True, blank=True)
    bairro = models.CharField(max_length=60)
    municipio = models.CharField(max_length=60)
    uf = models.CharField('UF', max_length=2)
    cep = models.CharField('CEP', max_length=8)
    telefones = models.CharField(max_length=60, null=True, blank=True)
    email = models.EmailField('E-mail', max_length=100, null=True, blank=True)
    nfe = models.BooleanField('NFe', default=False)
    nfce = models.BooleanField('NFCe', default=False)
    cte = models.BooleanField('CTe', default=False)
    mdfe = models.BooleanField('MDFe', default=False)
    token = models.CharField(max_length=64, null=True, blank=True)
    emissoes_ativo = models.BooleanField('Emissões Ativas', default=False)
    cadastro_ativo = models.BooleanField('Cadastro Ativo', default=True)

    def __str__(self):
        return self.nome