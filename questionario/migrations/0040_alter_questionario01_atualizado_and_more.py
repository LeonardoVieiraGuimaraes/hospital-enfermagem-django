# Generated by Django 4.1.7 on 2023-04-27 13:13

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0039_alter_questionario01_atualizado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionario01',
            name='atualizado',
            field=models.DateField(default='2023-04-27'),
        ),
        migrations.AlterField(
            model_name='questionario01',
            name='data_cadastro',
            field=models.DateField(default='2023-04-27'),
        ),
        migrations.AlterField(
            model_name='questionario01',
            name='data_cirurgia',
            field=models.DateField(default='2023-04-27'),
        ),
        migrations.AlterField(
            model_name='questionario0101',
            name='atualizado',
            field=models.DateField(default='2023-04-27'),
        ),
        migrations.AlterField(
            model_name='questionario0101',
            name='data_cadastro',
            field=models.DateField(default='2023-04-27'),
        ),
        migrations.AlterField(
            model_name='questionario0101',
            name='jejum_se_sim',
            field=models.TimeField(default='10:13'),
        ),
        migrations.AlterField(
            model_name='questionario0101',
            name='realizou_hemodialise_se_sim_02',
            field=models.DateField(default='2023-04-27'),
        ),
        migrations.AlterField(
            model_name='questionario0101',
            name='realizou_quimeoterapia_se_sim_02',
            field=models.DateField(default='2023-04-27'),
        ),
        migrations.AlterField(
            model_name='questionario0101',
            name='realizou_radioterapia_se_sim_02',
            field=models.DateField(default='2023-04-27'),
        ),
        migrations.AlterField(
            model_name='questionario0101',
            name='triconomia_realizada_se_sim_01',
            field=models.TimeField(default='10:13'),
        ),
        migrations.AlterField(
            model_name='questionario0102',
            name='antibiotico_profilatico_a_u_m_se_sim_01',
            field=models.TimeField(default='10:13', max_length=3),
        ),
        migrations.AlterField(
            model_name='questionario0102',
            name='atualizado',
            field=models.DateField(default='2023-04-27'),
        ),
        migrations.AlterField(
            model_name='questionario0102',
            name='data_cadastro',
            field=models.DateField(default='2023-04-27'),
        ),
        migrations.AlterField(
            model_name='questionario0102',
            name='data_vencimento',
            field=models.DateField(default='2023-04-27'),
        ),
        migrations.AlterField(
            model_name='questionario0102',
            name='hora_incisao_c',
            field=models.TimeField(default='10:13'),
        ),
        migrations.AlterField(
            model_name='questionario0103',
            name='data_cadastro',
            field=models.DateField(default='2023-04-27'),
        ),
        migrations.AlterField(
            model_name='questionario02',
            name='atualizado',
            field=models.DateField(default='2023-04-27'),
        ),
        migrations.AlterField(
            model_name='questionario02',
            name='data_cadastro',
            field=models.DateField(default='2023-04-27'),
        ),
        migrations.AlterField(
            model_name='questionario02',
            name='historia_progressa',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('HAS', 'HAS'), ('IAM', 'IAM'), ('Sedentarismo', 'Sedentarismo'), ('Tuberculose', 'Tuberculose'), ('Diabetes Mellitus', 'Diabetes Mellitus'), ('Hepatites', 'Hepatites'), ('Obesidade', 'Obesidade'), ('AVE', 'AVE')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='questionario02',
            name='nutricao',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Oral', 'Oral'), ('GTT', 'GTT'), ('SNE', 'SNE'), ('SNG', 'SNG')], default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='questionario02',
            name='qual_ingesta_hidrica_d',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Água', 'Água'), ('Sucos Naturais', 'Sucos Naturais'), ('Sucos Industrializados', 'Sucos Industrializados'), ('Refrigerantes', 'Refrigerantes'), ('Bebidas Alcoólicas', 'Bebidas Alcoólicas'), ('Água de Coco', 'Água de Coco')], default='', max_length=300),
        ),
    ]
