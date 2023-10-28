# Generated by Django 4.1.7 on 2023-03-13 12:19

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0026_alter_questionario0101_jejum_se_sim_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionario0101',
            name='jejum_se_sim',
            field=models.TimeField(default='9:19'),
        ),
        migrations.AlterField(
            model_name='questionario0101',
            name='triconomia_realizada_se_sim_01',
            field=models.TimeField(default='9:19'),
        ),
        migrations.AlterField(
            model_name='questionario0102',
            name='antibiotico_profilatico_a_u_m_se_sim_01',
            field=models.TimeField(default='9:19', max_length=3),
        ),
        migrations.AlterField(
            model_name='questionario0102',
            name='hora_incisao_c',
            field=models.TimeField(default='9:19'),
        ),
        migrations.AlterField(
            model_name='questionario02',
            name='historia_progressa',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('HAS', 'HAS'), ('IAM', 'IAM'), ('Sedentarismo', 'Sedentarismo'), ('Tuberculose', 'Tuberculose'), ('D.M.', 'D.M.'), ('Hepatites', 'Hepatites'), ('Obesidade', 'Obesidade'), ('AVE', 'AVE')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='questionario02',
            name='nivel_autonimia',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Alta', 'Alta'), ('Moderada', 'Moderada'), ('Pouca', 'Pouca'), ('Nenhuma', 'Nenhuma')], default='', max_length=50),
        ),
    ]
