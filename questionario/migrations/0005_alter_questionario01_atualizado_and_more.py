# Generated by Django 4.1.7 on 2023-02-22 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("questionario", "0004_alter_questionario01_atualizado_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="questionario01",
            name="atualizado",
            field=models.DateField(default="2023-02-22"),
        ),
        migrations.AlterField(
            model_name="questionario01",
            name="data_cadastro",
            field=models.DateField(default="2023-02-22"),
        ),
        migrations.AlterField(
            model_name="questionario01",
            name="data_cirurgia",
            field=models.DateField(default="2023-02-22"),
        ),
        migrations.AlterField(
            model_name="questionario0101",
            name="atualizado",
            field=models.DateField(default="2023-02-22"),
        ),
        migrations.AlterField(
            model_name="questionario0101",
            name="data_cadastro",
            field=models.DateField(default="2023-02-22"),
        ),
        migrations.AlterField(
            model_name="questionario0101",
            name="jejum_se_sim",
            field=models.TimeField(default="10:43"),
        ),
        migrations.AlterField(
            model_name="questionario0101",
            name="realizou_hemodialise_se_sim_02",
            field=models.DateField(default="2023-02-22"),
        ),
        migrations.AlterField(
            model_name="questionario0101",
            name="realizou_quimeoterapia_se_sim_02",
            field=models.DateField(default="2023-02-22"),
        ),
        migrations.AlterField(
            model_name="questionario0101",
            name="realizou_radioterapia_se_sim_02",
            field=models.DateField(default="2023-02-22"),
        ),
        migrations.AlterField(
            model_name="questionario0101",
            name="triconomia_realizada_se_sim_01",
            field=models.TimeField(default="10:43"),
        ),
        migrations.CreateModel(
            name="Questionario0102",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("todos_membros_e_e_p", models.CharField(default="", max_length=1)),
                ("nome_paciente", models.CharField(default="", max_length=1)),
                ("sitio_cirurgico", models.CharField(default="", max_length=1)),
                ("procedimento", models.CharField(default="", max_length=1)),
                ("lateralidade", models.CharField(default="", max_length=1)),
                ("antes_assepsia_c_o", models.CharField(default="", max_length=1)),
                (
                    "antes_assepsia_c_o_se_sim",
                    models.CharField(default="", max_length=1),
                ),
                (
                    "antibiotico_profilatico_a_u_m",
                    models.CharField(default="", max_length=1),
                ),
                (
                    "antibiotico_profilatico_a_u_m_se_sim_01",
                    models.TimeField(default="10:43", max_length=1),
                ),
                ("hora_incisao_c", models.TimeField(default="10:43")),
                ("placa_bisturi_p", models.CharField(default="", max_length=1)),
                (
                    "materiais_instumentais_c_d",
                    models.CharField(default="", max_length=1),
                ),
                (
                    "materiais_instumentais_c_d_se_sim_01",
                    models.CharField(default="", max_length=50),
                ),
                ("fita_indicador_q_m", models.CharField(default="", max_length=1)),
                ("integrador_material", models.CharField(default="", max_length=1)),
                ("data_vencimento", models.DateField(default="2023-02-22")),
                ("cirurgia_realizada", models.CharField(default="", max_length=50)),
                (
                    "registro_completo_p_r_l_p",
                    models.CharField(default="", max_length=50),
                ),
                ("data_cadastro", models.DateField(default="2023-02-22")),
                ("atualizado", models.DateField(default="2023-02-22")),
                (
                    "cirurgia_segura",
                    models.OneToOneField(
                        default="",
                        on_delete=django.db.models.deletion.PROTECT,
                        to="questionario.questionario01",
                    ),
                ),
            ],
        ),
    ]
