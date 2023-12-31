# Generated by Django 4.1.7 on 2023-03-27 16:06

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0031_alter_questionario0101_jejum_se_sim_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionario02',
            name='anotacoes_adicionais',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='questionario02',
            name='novel_consciencia',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Consciente', 'Consciente'), ('Orientada(o)', 'Orientada(o)'), ('Desorientada(o)', 'Desorientada(o)')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='questionario01',
            name='atualizado',
            field=models.DateField(default='2023-03-27'),
        ),
        migrations.AlterField(
            model_name='questionario01',
            name='data_cadastro',
            field=models.DateField(default='2023-03-27'),
        ),
        migrations.AlterField(
            model_name='questionario01',
            name='data_cirurgia',
            field=models.DateField(default='2023-03-27'),
        ),
        migrations.AlterField(
            model_name='questionario0101',
            name='atualizado',
            field=models.DateField(default='2023-03-27'),
        ),
        migrations.AlterField(
            model_name='questionario0101',
            name='data_cadastro',
            field=models.DateField(default='2023-03-27'),
        ),
        migrations.AlterField(
            model_name='questionario0101',
            name='jejum_se_sim',
            field=models.TimeField(default='13:6'),
        ),
        migrations.AlterField(
            model_name='questionario0101',
            name='realizou_hemodialise_se_sim_02',
            field=models.DateField(default='2023-03-27'),
        ),
        migrations.AlterField(
            model_name='questionario0101',
            name='realizou_quimeoterapia_se_sim_02',
            field=models.DateField(default='2023-03-27'),
        ),
        migrations.AlterField(
            model_name='questionario0101',
            name='realizou_radioterapia_se_sim_02',
            field=models.DateField(default='2023-03-27'),
        ),
        migrations.AlterField(
            model_name='questionario0101',
            name='triconomia_realizada_se_sim_01',
            field=models.TimeField(default='13:6'),
        ),
        migrations.AlterField(
            model_name='questionario0102',
            name='antibiotico_profilatico_a_u_m_se_sim_01',
            field=models.TimeField(default='13:6', max_length=3),
        ),
        migrations.AlterField(
            model_name='questionario0102',
            name='atualizado',
            field=models.DateField(default='2023-03-27'),
        ),
        migrations.AlterField(
            model_name='questionario0102',
            name='data_cadastro',
            field=models.DateField(default='2023-03-27'),
        ),
        migrations.AlterField(
            model_name='questionario0102',
            name='data_vencimento',
            field=models.DateField(default='2023-03-27'),
        ),
        migrations.AlterField(
            model_name='questionario0102',
            name='hora_incisao_c',
            field=models.TimeField(default='13:6'),
        ),
        migrations.AlterField(
            model_name='questionario0103',
            name='data_cadastro',
            field=models.DateField(default='2023-03-27'),
        ),
        migrations.AlterField(
            model_name='questionario02',
            name='alergias_out',
            field=models.TextField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='questionario02',
            name='alteracao_paladar_se_sim',
            field=models.TextField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='questionario02',
            name='apresenta_mucosite_se_sim',
            field=models.TextField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='questionario02',
            name='atualizado',
            field=models.DateField(default='2023-03-27'),
        ),
        migrations.AlterField(
            model_name='questionario02',
            name='data_cadastro',
            field=models.DateField(default='2023-03-27'),
        ),
        migrations.AlterField(
            model_name='questionario02',
            name='sinais_sintomas_fisicos',
            field=models.TextField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='questionario02',
            name='tem_acompanhemento',
            field=models.CharField(default='', max_length=3),
        ),
        migrations.AlterField(
            model_name='questionario02',
            name='tratamento_realizado_out',
            field=models.TextField(default='', max_length=200),
        ),
    ]
