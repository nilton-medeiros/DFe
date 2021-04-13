# Generated by Django 3.2 on 2021-04-12 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emitente', '0002_emitente_token'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emitente',
            old_name='cob_bairro',
            new_name='cobranca_bairro',
        ),
        migrations.RenameField(
            model_name='emitente',
            old_name='cob_cep',
            new_name='cobranca_cep',
        ),
        migrations.RenameField(
            model_name='emitente',
            old_name='cob_complemento',
            new_name='cobranca_logradouro',
        ),
        migrations.RenameField(
            model_name='emitente',
            old_name='cob_fones',
            new_name='cobranca_municipio',
        ),
        migrations.RenameField(
            model_name='emitente',
            old_name='cob_numero',
            new_name='cobranca_numero',
        ),
        migrations.RenameField(
            model_name='emitente',
            old_name='cob_uf',
            new_name='cobranca_uf',
        ),
        migrations.RemoveField(
            model_name='emitente',
            name='cob_logradouro',
        ),
        migrations.RemoveField(
            model_name='emitente',
            name='cob_municipio',
        ),
        migrations.AddField(
            model_name='emitente',
            name='cobranca_complemento',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='emitente',
            name='cobranca_fones',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='emitente',
            name='cnpj',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='emitente',
            name='cpf',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='emitente',
            name='inscricao_estadual',
            field=models.CharField(max_length=14, null=True),
        ),
    ]