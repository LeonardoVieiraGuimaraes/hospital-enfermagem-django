# Generated by Django 4.1.7 on 2023-03-09 14:05

import multiselectfield.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('questionario', '0015_remove_questionario0102_registro_completo_p_r_l_p_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionario0101',
            name='jejum_se_sim',
            field=models.TimeField(default='11:5'),
        ),
        migrations.AlterField(
            model_name='questionario0101',
            name='triconomia_realizada_se_sim_01',
            field=models.TimeField(default='11:5'),
        ),
        migrations.AlterField(
            model_name='questionario0102',
            name='antibiotico_profilatico_a_u_m_se_sim_01',
            field=models.TimeField(default='11:5', max_length=3),
        ),
        migrations.AlterField(
            model_name='questionario0102',
            name='hora_incisao_c',
            field=models.TimeField(default='11:5'),
        ),
        migrations.AlterField(
            model_name='questionario02',
            name='apresenta',
            field=multiselectfield.db.fields.MultiSelectField(
                choices=[('item_key1', 'Item title 1.1'), ('item_key2', 'Item title 1.2'),
                         ('item_key3', 'Item title 1.3'), ('item_key4', 'Item title 1.4'),
                         ('item_key5', 'Item title 1.5')], default='', max_length=300),
        ),
    ]