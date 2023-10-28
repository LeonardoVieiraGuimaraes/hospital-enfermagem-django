# Generated by Django 4.1.7 on 2023-03-04 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("questionario", "0009_alter_questionario0101_jejum_se_sim_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="questionario02",
            old_name="alteracao_paladar_se_sim",
            new_name="alteracao_paladar_se_sim_01",
        ),
        migrations.RenameField(
            model_name="questionario02",
            old_name="apresenta_mucosite_se_sim",
            new_name="apresenta_mucosite_se_sim_01",
        ),
        migrations.RemoveField(
            model_name="questionario0103",
            name="atualizado",
        ),
        migrations.AddField(
            model_name="questionario02",
            name="atualizado",
            field=models.DateField(default="2023-03-04"),
        ),
        migrations.AlterField(
            model_name="questionario01",
            name="atualizado",
            field=models.DateField(default="2023-03-04"),
        ),
        migrations.AlterField(
            model_name="questionario01",
            name="data_cadastro",
            field=models.DateField(default="2023-03-04"),
        ),
        migrations.AlterField(
            model_name="questionario01",
            name="data_cirurgia",
            field=models.DateField(default="2023-03-04"),
        ),
        migrations.AlterField(
            model_name="questionario0101",
            name="atualizado",
            field=models.DateField(default="2023-03-04"),
        ),
        migrations.AlterField(
            model_name="questionario0101",
            name="data_cadastro",
            field=models.DateField(default="2023-03-04"),
        ),
        migrations.AlterField(
            model_name="questionario0101",
            name="jejum_se_sim",
            field=models.TimeField(default="11:4"),
        ),
        migrations.AlterField(
            model_name="questionario0101",
            name="realizou_hemodialise_se_sim_02",
            field=models.DateField(default="2023-03-04"),
        ),
        migrations.AlterField(
            model_name="questionario0101",
            name="realizou_quimeoterapia_se_sim_02",
            field=models.DateField(default="2023-03-04"),
        ),
        migrations.AlterField(
            model_name="questionario0101",
            name="realizou_radioterapia_se_sim_02",
            field=models.DateField(default="2023-03-04"),
        ),
        migrations.AlterField(
            model_name="questionario0101",
            name="triconomia_realizada_se_sim_01",
            field=models.TimeField(default="11:4"),
        ),
        migrations.AlterField(
            model_name="questionario0102",
            name="antibiotico_profilatico_a_u_m_se_sim_01",
            field=models.TimeField(default="11:4", max_length=3),
        ),
        migrations.AlterField(
            model_name="questionario0102",
            name="atualizado",
            field=models.DateField(default="2023-03-04"),
        ),
        migrations.AlterField(
            model_name="questionario0102",
            name="data_cadastro",
            field=models.DateField(default="2023-03-04"),
        ),
        migrations.AlterField(
            model_name="questionario0102",
            name="data_vencimento",
            field=models.DateField(default="2023-03-04"),
        ),
        migrations.AlterField(
            model_name="questionario0102",
            name="hora_incisao_c",
            field=models.TimeField(default="11:4"),
        ),
        migrations.AlterField(
            model_name="questionario0103",
            name="data_cadastro",
            field=models.DateField(default="2023-03-04"),
        ),
        migrations.AlterField(
            model_name="questionario02",
            name="data_cadastro",
            field=models.DateField(default="2023-03-04"),
        ),
    ]
