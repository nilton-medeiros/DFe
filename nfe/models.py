from django.db import models
from uuid import uuid4

from emitentes.models import Emitente


def upload_file_nfe(instance, filename):
    if Emitente.cnpj:
        doc = Emitente.cnpj
    else:
        doc = Emitente.cpf
    path: str = f"{doc}/nfe/{filename[filename.rfind('.')+1:].upper()}s/"
    path += str(instance.data_emissao.year) + '/' + str(instance.data_emissao.month) + '/' + filename
    return path


# Controle de NFe's do ambiente de Produção
class Nfe(models.Model):
    # Este id do tipo token (UUID4) é retornado ao solicitante como ref (referencia) a esta NFe para consultas
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    emitente_id = models.ForeignKey(Emitente, on_delete=models.CASCADE)
    serie = models.IntegerField('Série NFe', default=1)
    numero = models.IntegerField('Número NFe', default=1)
    numero_carta_correcao = models.IntegerField('Número Carta Cor.', default=0)
    chave = models.CharField('Chave NFe', max_length=44)
    data_emissao = models.DateField('Emitido Em')
    situacao = models.CharField('Situação', max_length=25)
    status_sefaz = models.CharField('Status Sefaz', max_length=3)
    mensagem_sefaz = models.CharField('Mensagem Sefaz', max_length=300)
    url_xml_nfe = models.FileField(upload_to=upload_file_nfe, null=True, blank=True)
    url_pdf_nfe = models.FileField(upload_to=upload_file_nfe, null=True, blank=True)
    url_xml_cancelado = models.FileField(upload_to=upload_file_nfe, null=True, blank=True)
    url_pdf_cancelado = models.FileField(upload_to=upload_file_nfe, null=True, blank=True)
    url_xml_carta_correcao = models.FileField(upload_to=upload_file_nfe, null=True, blank=True)
    url_pdf_carta_correcao = models.FileField(upload_to=upload_file_nfe, null=True, blank=True)
