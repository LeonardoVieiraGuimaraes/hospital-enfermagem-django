# Generated by Django 4.1.7 on 2023-03-13 12:16

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0025_alter_questionario01_atualizado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionario0101',
            name='jejum_se_sim',
            field=models.TimeField(default='9:16'),
        ),
        migrations.AlterField(
            model_name='questionario0101',
            name='triconomia_realizada_se_sim_01',
            field=models.TimeField(default='9:16'),
        ),
        migrations.AlterField(
            model_name='questionario0102',
            name='antibiotico_profilatico_a_u_m_se_sim_01',
            field=models.TimeField(default='9:16', max_length=3),
        ),
        migrations.AlterField(
            model_name='questionario0102',
            name='hora_incisao_c',
            field=models.TimeField(default='9:16'),
        ),
        migrations.AlterField(
            model_name='questionario02',
            name='alergias',
            field=models.CharField(choices=[('Medicamentosa', 'Medicamentosa'), ('Alimentar', 'Alimentar'), ('Respiratória', 'Respiratória'), ('Cutânea', 'Cutânea'), ('Out', 'Outras')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='questionario02',
            name='historia_progressa',
            field=models.CharField(choices=[('HAS', 'HAS'), ('IAM', 'IAM'), ('Sedentarismo', 'Sedentarismo'), ('Tuberculose', 'Tuberculose'), ('D.M.', 'D.M.'), ('Hepatites', 'Hepatites'), ('Obesidade', 'Obesidade'), ('AVE', 'AVE')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='questionario02',
            name='nivel_autonimia',
            field=models.CharField(choices=[('Alta', 'Alta'), ('Moderada', 'Moderada'), ('Pouca', 'Pouca'), ('Nenhuma', 'Nenhuma')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='questionario02',
            name='nutricao',
            field=models.CharField(choices=[('Oral', 'Oral'), ('GTT', 'GTT'), ('SNE', 'SNE'), ('CNG', 'CNG')], default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='questionario02',
            name='possiveis_sinais_sintomas_rt',
            field=models.CharField(choices=[('Diarreia', 'Diarreia'), ('Constipação', 'Constipação'), ('Tosse', 'Tosse'), ('Dispnéia', 'Dispnéia'), ('Palpitação', 'Palpitação'), ('Prurido', 'Prurido'), ('Náusea', 'Náusea'), ('Êmese', 'Êmese'), ('Astenia', 'Astenia'), ('Inapetência', 'Inapetência'), ('Anorexia', 'Anorexia'), ('Edema', 'Edema'), ('Infecção', 'Infecção'), ('Síncope', 'Síncope'), ('Alteração Motora', 'Alteração Motora'), ('Sangramento', 'Sangramento'), ('Alteração Circulatória', 'Alteração Circulatória')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='questionario02',
            name='possui_alguma_dessas_d',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Dificuldade em Deglutir', 'Dificuldade em Deglutir'), ('Dificuldade para Mastigação', 'Dificuldade para Mastigação'), ('Êmese', 'Êmese'), ('Náusea', 'Náusea')], default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='questionario02',
            name='qual_ingesta_hidrica_d',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Água', 'Água'), ('Sucos Naturais', 'Sucos Naturais'), ('Sucos Industrializados', 'Sucos Industrializados'), ('Refrigerantes', 'Refrigerantes'), ('Bebidas', 'Bebidas'), ('Alcoólicas', 'Alcoólicas'), ('Água de Coco', 'Água de Coco')], default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='questionario02',
            name='tratamento_realizado',
            field=models.CharField(choices=[('Quimioterapia', 'Quimioterapia'), ('Radioterapia', 'Radioterapia'), ('Cirurgia', 'Cirurgia'), ('Out', 'Outro')], default='', max_length=50),
        ),
    ]
