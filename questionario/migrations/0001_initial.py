# Generated by Django 4.1.6 on 2023-02-17 20:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("usuario", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Questionario01",
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
                ("cirurgia_proposta", models.CharField(default="", max_length=50)),
                ("sala_cirurgica", models.CharField(default="", max_length=50)),
                ("data_cirurgia", models.DateField(default="2023-02-17")),
                ("modalidade", models.CharField(default="", max_length=10)),
                ("comorbidade", models.CharField(default="", max_length=50)),
                ("data_cadastro", models.DateField(default="2023-02-17")),
                ("atualizado", models.DateField(default="2023-02-17")),
                (
                    "paciente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="usuario.paciente",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Questionario0101",
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
                ("pulseira_identificacao", models.CharField(default="", max_length=1)),
                ("prontuario_completo", models.CharField(default="", max_length=1)),
                (
                    "prontuario_completo_se_nao",
                    models.CharField(default="", max_length=100),
                ),
                ("possui_dispositivos", models.CharField(default="", max_length=1)),
                (
                    "possui_dispositivos_se_sim",
                    models.CharField(default="", max_length=100),
                ),
                ("procedimento_confirmado", models.CharField(default="", max_length=1)),
                ("termo_consentimento_c_a", models.CharField(default="", max_length=1)),
                ("exames_laborat_i_d", models.CharField(default="", max_length=1)),
                ("risco_perda_s", models.CharField(default="", max_length=1)),
                ("resserva_hemoderivados", models.CharField(default="", max_length=1)),
                ("resserva_CTI", models.CharField(default="", max_length=1)),
                ("sitio_cirurgico_d", models.CharField(default="", max_length=1)),
                ("jejum", models.CharField(default="", max_length=1)),
                ("jejum_se_sim", models.TimeField(default=datetime.time)),
                ("alergia_conhecida", models.CharField(default="", max_length=1)),
                (
                    "alergia_conhecida_se_sim",
                    models.CharField(default="", max_length=20),
                ),
                ("triconomia_realizada", models.CharField(default="", max_length=1)),
                (
                    "triconomia_realizada_se_sim_01",
                    models.TimeField(default=datetime.time),
                ),
                (
                    "triconomia_realizada_se_sim_02",
                    models.CharField(default="", max_length=11),
                ),
                (
                    "triconomia_realizada_se_sim_03",
                    models.CharField(default="", max_length=20),
                ),
                ("realizou_quimeoterapia", models.CharField(default="", max_length=1)),
                (
                    "realizou_quimeoterapia_se_sim_01",
                    models.PositiveIntegerField(default=0),
                ),
                (
                    "realizou_quimeoterapia_se_sim_02",
                    models.DateField(default="2023-02-17"),
                ),
                ("realizou_radioterapia", models.CharField(default="", max_length=1)),
                (
                    "realizou_radioterapia_se_sim_01",
                    models.PositiveIntegerField(default=0),
                ),
                (
                    "realizou_radioterapia_se_sim_02",
                    models.DateField(default="2023-02-17"),
                ),
                ("realizou_hemodialise", models.CharField(default="", max_length=1)),
                (
                    "realizou_hemodialise_se_sim_01",
                    models.PositiveIntegerField(default=0),
                ),
                (
                    "realizou_hemodialise_se_sim_02",
                    models.DateField(default="2023-02-17"),
                ),
                ("realizou_transplante_o", models.CharField(default="", max_length=1)),
                (
                    "realizou_transplante_o_se_sim",
                    models.PositiveIntegerField(default=0),
                ),
                (
                    "verificacao_anestesica_m_v_m_e_a",
                    models.CharField(default="", max_length=1),
                ),
                (
                    "verificacao_anestesica_m_v_m_e_a_se_nao",
                    models.PositiveIntegerField(default=0),
                ),
                ("vias_aereas_d_r_a", models.CharField(default="", max_length=1)),
                ("tempo_previsto_cirurgia", models.CharField(default="", max_length=1)),
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
