# Generated by Django 4.1.7 on 2023-03-31 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0012_alter_colaborador_atualizado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='atualizado',
            field=models.DateField(verbose_name='2023-03-31'),
        ),
        migrations.AlterField(
            model_name='colaborador',
            name='data_cadastro',
            field=models.DateField(verbose_name='2023-03-31'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='data_nascimento',
            field=models.DateField(verbose_name='2023-03-31'),
        ),
    ]
