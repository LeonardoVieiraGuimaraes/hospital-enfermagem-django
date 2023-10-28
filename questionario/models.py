from datetime import date, datetime

from django.db import models
from multiselectfield import MultiSelectField

from usuario.models import Paciente


# Create your models here.

####################### ENTRADA ANTES DA INDUÇÃO ANESTESISCA ##########################

####################### CADASTRO DA CIRURGIA SEGURA ##########################


class Questionario01(models.Model):
    date = str(date.today())
    datenow = datetime.now()

    time = f"{datenow.hour}:{datenow.minute}"

    # Paciente
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    # CIRURGIA PROPOSTA
    cirurgia_proposta = models.CharField(max_length=50, default='')

    # Sala Cirurgica:
    sala_cirurgica = models.CharField(max_length=50, default='')

    # Data da Cirurgia:
    data_cirurgia = models.DateField(default=date)
    # Modalidade ( ) Eletiva (  )Urgência ( )Emergência
    modalidade = models.CharField(
        max_length=30, default='')

    # COMORBIDADE
    comorbidade = models.CharField(max_length=50, default='')

    data_cadastro = models.DateField(default=date)

    atualizado = models.DateField(default=date)

    def __str__(self):
        return str(self.paciente)


class Questionario0101(models.Model):
    date = str(date.today())
    datenow = datetime.now()

    time = f"{datenow.hour}:{datenow.minute}"

    # Paciente
    cirurgia_segura = models.OneToOneField(Questionario01, on_delete=models.PROTECT, default="")

    # usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)

    # Pulseira de identificação  ( ) S  (  ) N
    pulseira_identificacao = models.CharField(max_length=3, default='')

    #   PRONTUARIO COMPLETO:  (   ) SIM (   ) NÃO
    # QUAIS DOCUMENTOS FALTAM:-------------------------

    prontuario_completo = models.CharField(max_length=3, default="")
    prontuario_completo_se_nao = models.CharField(max_length=300, default="")

    #  POSSUI  DISPOSITIVOS : (  ) SIM   (  ) NÃO
    # QUAIS ?
    possui_dispositivos = models.CharField(max_length=3, default="")
    possui_dispositivos_se_sim = models.CharField(max_length=300, default="")

    # PROCEDIEMNTOS CONFIRMADO: (  ) SIM (  ) NÃO
    procedimento_confirmado = models.CharField(max_length=3, default='')

    # Termo de Consentimento Cirúrgico e Anestésico: () sim() não
    termo_consentimento_c_a = models.CharField(max_length=3, default='')

    #    Exame: ( Laborat. Imagens disponível: ( ) sim ( ) não
    exames_laborat_i_d = models.CharField(max_length=3, default='')

    # RISCO DE PERDA SANGUINEA+ 500ML:  (  ) SIM (  ) NÃO
    risco_perda_s = models.CharField(max_length=3, default='')

    # RESSERVA DE HEMODERIVADOS:  (  ) SIM (  ) NÃO
    resserva_hemoderivados = models.CharField(max_length=3, default='')

    # Reserva de CTI: () sim() não

    resserva_CTI = models.CharField(max_length=3, default='')

    # SITIO CIRURGICO DEMARCADO:  (  ) SIM (  ) NÃO
    sitio_cirurgico_d = models.CharField(max_length=3, default='')

    # Jejum ( ) S - inicio ______ ( )  N
    jejum = models.CharField(max_length=3, default='')
    jejum_se_sim = models.TimeField(default=time)

    # Alergia conhecida: : ( ) sim ( ) não / Se sim Qual?
    alergia_conhecida = models.CharField(max_length=3, default='')
    alergia_conhecida_se_sim = models.CharField(max_length=20, default='')

    # TRICOTOMIA: (  ) SIM (  ) NÃO (  )  NA ,
    # HORA: -------
    # QUAL MEIO: (  ) APARADOR  (  ) BARBEADOR
    # LOCAL: (  ) BLOCO CIRURGICO  (  ) CLINICA

    triconomia_realizada = models.CharField(max_length=3, default='')
    triconomia_realizada_se_sim_01 = models.TimeField(
        default=time)
    triconomia_realizada_se_sim_02 = models.CharField(
        max_length=31, default="")
    triconomia_realizada_se_sim_03 = models.CharField(
        max_length=20, default="")

    # Relizou Quimeoterapia : ( ) N ( ) S Quantas sessões ___ ultima sessão
    realizou_quimeoterapia = models.CharField(
        max_length=3, default='')
    realizou_quimeoterapia_se_sim_01 = models.PositiveIntegerField(default=0)
    realizou_quimeoterapia_se_sim_02 = models.DateField(
        default=date)

    # Realizou Radioterapia: ( ) N ( ) S Quantas sessões ___ ultima sessão
    realizou_radioterapia = models.CharField(max_length=3, default='')
    realizou_radioterapia_se_sim_01 = models.PositiveIntegerField(default=0)
    realizou_radioterapia_se_sim_02 = models.DateField(
        default=date)

    #     REALIZOU HEMODIALISE: (  ) SIM (  ) NÃO
    # QUANTAS SESSÕES:
    # ULTIMA SESSÃO:
    realizou_hemodialise = models.CharField(max_length=3, default='')
    realizou_hemodialise_se_sim_01 = models.PositiveIntegerField(default=0)
    realizou_hemodialise_se_sim_02 = models.DateField(default=date)

    # REALIZOU TRANSPLANTE DE ÓRGAO: (  ) SIM  (  ) NÃO
    # QUAL ANO: ----------
    realizou_transplante_o = models.CharField(max_length=3, default='')
    realizou_transplante_o_se_sim = models.PositiveIntegerField(default=0)

    # Verificação Anestésica: Materiais VAD, Medicações e Equipamentos adequados:
    # () sim() não / Se Não Qual?

    verificacao_anestesica_m_v_m_e_a = models.CharField(max_length=3, default='')
    verificacao_anestesica_m_v_m_e_a_se_nao = models.PositiveIntegerField(default=0)

    # Vias Aéreas difíceis ou risco de Aspiração: () sim() não
    vias_aereas_d_r_a = models.CharField(
        max_length=3, default='')

    # Tempo previsto para cirurgia() sim() não
    tempo_previsto_cirurgia = models.CharField(
        max_length=3, default='')

    data_cadastro = models.DateField(default=date)

    atualizado = models.DateField(default=date)

    def __str__(self):
        return str(self.cirurgia_segura)


# ##############################################################
# PAUSA# – ANTES DA INCISÃO CIRURGICA

class Questionario0102(models.Model):
    date = str(date.today())
    datenow = datetime.now()
    time = f"{datenow.hour}:{datenow.minute}"

    #  TODOS OS MEMBROS DA EQUIPE ESTÃO PRESENTES: (  ) SIM (  ) NÃO

    cirurgia_segura = models.OneToOneField(Questionario01, on_delete=models.PROTECT, default="")

    # Todos os Membros da equipe estão presentaes () sim () não
    todos_membros_e_e_p = models.CharField(max_length=3, default='')
    # TODOS CONFIRMAM NOVAMENTE :
    # NOME DO PACIENTE  (  ) SIM ( ) NÃO
    nome_paciente = models.CharField(max_length=3, default='')

    # SITITO CIRURGICO:  (  ) SIM (  ) NÃO
    sitio_cirurgico = models.CharField(max_length=3, default='')

    # PROCEDIMENTO;  (  ) SIM (  ) NÃO
    procedimento = models.CharField(max_length=3, default='')

    # LATERALIDADE:  (  ) SIM (  ) NÃO
    lateralidade = models.CharField(max_length=3, default='')

    # ANTE ASSEPSIA DO CAMPO OPERATÓRIO:  (  ) SIM (  ) NÃO
    # SE SIM QUAL O PRODUTO?
    antes_assepsia_c_o = models.CharField(max_length=3, default='')
    antes_assepsia_c_o_se_sim = models.CharField(max_length=20, default='')

    # O ANTIBIOTICO PROFILÁTICO FOI ADMINISTRADO NOS ULTIMOS 60 MINUTOS:   (  ) SIM  (  ) NÃO ( ) Na
    # se sim, hora:

    antibiotico_profilatico_a_u_m = models.CharField(max_length=3, default='')
    antibiotico_profilatico_a_u_m_se_sim_01 = models.TimeField(
        max_length=3, default=time)

    # Hora da Incisão cirúrgica: _________
    hora_incisao_c = models.TimeField(default=time)

    # Placa de bisturi posicionado? ( ) sim() não() NA
    placa_bisturi_p = models.CharField(max_length=3, default='')

    # Materiais e instrumentais conferidos e disponível: ( ) sim ( ) não Se sim, quais? _______

    materiais_instumentais_c_d = models.CharField(max_length=3, default='')
    materiais_instumentais_c_d_se_sim_01 = models.CharField(max_length=50, default='')

    # fita indicadora química do material: ( ) sim ( )não
    fita_indicador_q_m = models.CharField(max_length=3, default='')

    # integrador do material: ( ) sim ( ) não
    integrador_material = models.CharField(max_length=3, default='')

    # Data do vencimento
    data_vencimento = models.DateField(default=date)

    # cirurgia realizada ___________________

    cirurgia_realizada = models.CharField(max_length=50, default='')

    # # Registro completo e peças registradas no livro de procedimento ( ) sim ( ) não
    #
    # registro_completo_p_r_l_p = models.CharField(max_length=50, default='')

    data_cadastro = models.DateField(default=date)

    atualizado = models.DateField(default=date)


# ##############################################################
# SAIDA- ANTES DO PACIENTESAIR DA SALA ( Contagem de Materiais Abertos )

class Questionario0103(models.Model):
    date = str(date.today())
    datenow = datetime.now()
    time = f"{datenow.hour}:{datenow.minute}"

    cirurgia_segura = models.OneToOneField(Questionario01, on_delete=models.PROTECT, default="")
    ###########################################################
    # CONTAGEM :
    # INSTRUMENTAIS  : ANTES :  --------  DEPOIS --------

    # COMPRESSAS:   ANTES :  -------- DEPOIS --------
    # AGULHAS  : ANTES :  ------ DEPOIS --------
    # Lâmina de Bisturi : Antes: _______ Depois: _____________
    instrumentais_antes = models.PositiveIntegerField(default=0)
    compressas_antes = models.PositiveIntegerField(default=0)
    agulhas_antes = models.PositiveIntegerField(default=0)
    lamina_bisturi_antes = models.PositiveIntegerField(default=0)

    instrumentais_depois = models.PositiveIntegerField(default=0)
    compressas_depois = models.PositiveIntegerField(default=0)
    agulhas_depois = models.PositiveIntegerField(default=0)
    lamina_bisturi_depois = models.PositiveIntegerField(default=0)

    # CIRÚRGIA REALIZADA: -----------------------------------
    cirurgia_realizada = models.CharField(max_length=50, default='')

    # REGISTRO COMPLETO DO PROCEDIMENTO  E PEÇAS NO LIVRO DE PROCEDIMENTO (  ) SIM (  ) NÃO
    registro_completo_p_p_l_p = models.CharField(max_length=3, default='')

    # HOUVE ALGUM PROBLEMA COM MATERIAIS, EQUIPAMENTOS E INSTRUMENTOS : (  )SIM (  )NÃO
    houve_algum_p_m_e_i = models.CharField(max_length=3, default='')

    # PEÇA PATOLOGICA: (  ) SIM (  ) NÃO
    peca_patologica = models.CharField(max_length=3, default='')

    # AMOSTRA DE CULTURA: (  ) SIM (  ) NÃO
    amostra_cultura = models.CharField(max_length=3, default='')

    # CITOLOGIA ONCOTICA: (  ) SIM  (  ) NÃO
    citologia_oncotica = models.CharField(max_length=3, default='')

    # AMOSTRA DE  LCR: líquido cefalorraquidiano (  ) SIM (  ) NÃO
    amostra_lcr = models.CharField(max_length=3, default='')

    #############################################################
    # CIÚRGIÃO, ANESTESISTA E ENFERMAGEM CONFIMAM
    # ALTA CONFIRMADA : (  ) RPAn(   ) CTI (  ) ENFERMARIA (  )ÒBITO

    alta_confirmada = models.CharField(max_length=35, default='')

    # OBSERVAÇÕES: --------------------------------------------------------------------
    observacoes = models.TextField(max_length=200, default="")

    # Cirurgião _______________________
    cirurgiao = models.CharField(max_length=50, default='')

    # Anestesista _______________________
    anestesista = models.CharField(max_length=50, default='')
    # Enfermeiro _______________________
    enfermeiro = models.CharField(max_length=50, default='')
    # Circulante_______________________
    circulante = models.CharField(max_length=50, default='')

    data_cadastro = models.DateField(default=date)

    # atualizado = models.DateField(default=date)

    def __str__(self):
        return str(self.cirurgia_segura)


####################### Questionário 02 ##########################
class Questionario02(models.Model):
    date = str(date.today())
    datenow = datetime.now()
    time = f"{datenow.hour}:{datenow.minute}"

    choices_possiveis_sinais_sintomas_rt = (
        ("Diarreia", "Diarreia"),
        ("Constipação", "Constipação"),
        ("Tosse", "Tosse"),
        ("Dispnéia", "Dispnéia"),
        ("Palpitação", "Palpitação"),
        ("Prurido", "Prurido"),
        ("Náusea", "Náusea"),
        ("Êmese", "Êmese"),
        ("Astenia", "Astenia"),
        ("Inapetência", "Inapetência"),
        ("Anorexia", "Anorexia"),
        ("Edema", "Edema"),
        ("Infecção", "Infecção"),
        ("Síncope", "Síncope"),
        ("Alteração Motora", "Alteração Motora"),
        ("Sangramento", "Sangramento"),
        ("Alteração Circulatória", "Alteração Circulatória")
    )

    choices_nivel_autonimia = (
        ("Alta", "Alta"),
        ("Moderada", "Moderada"),
        ("Pouca", "Pouca"),
        ("Nenhuma", "Nenhuma"),
    )

    choices_tratamento_realizado = (
        ("Quimioterapia", "Quimioterapia"),
        ("Radioterapia", "Radioterapia"),
        ("Cirurgia", "Cirurgia"),
        ("Out", "Outro")
    )

    choices_historia_progressa = (
        ("HAS", "HAS"),
        ("IAM", "IAM"),
        ("Sedentarismo", "Sedentarismo"),
        ("Tuberculose", "Tuberculose"),
        ("Diabetes Mellitus", "Diabetes Mellitus"),
        ("Hepatites", "Hepatites"),
        ("Obesidade", "Obesidade"),
        ("AVE", "AVE")
    )

    choices_alergias = (
        ("Medicamentosa", "Medicamentosa"),
        ("Alimentar", "Alimentar"),
        ("Respiratória", "Respiratória"),
        ("Cutânea", "Cutânea"),
        ("Out", "Outras")
    )

    choices_sn = (
        ("Sim", "Sim"),
        ("Não", "Não")
    )

    choices_nutricao = (
        ("Oral", "Oral"),
        ("GTT", "GTT"),
        ("SNE", "SNE"),
        ("SNG", "SNG")
    )

    choices_possui_alguma_dessas_d = (
        ("Dificuldade em Deglutir", "Dificuldade em Deglutir"),
        ("Dificuldade para Mastigação", "Dificuldade para Mastigação"),
        ("Êmese", "Êmese"),
        ("Náusea", "Náusea")
    )

    choices_qual_ingesta_hidrica_d = (
        ("Água", "Água"),
        ("Sucos Naturais", "Sucos Naturais"),
        ("Sucos Industrializados", "Sucos Industrializados"),
        ("Refrigerantes", "Refrigerantes"),
        ("Bebidas Alcoólicas", "Bebidas Alcoólicas"),
        ("Água de Coco", "Água de Coco")
    )

    choices_apresenta = (
        ("Desidratação", "Desidratação"),
        ("Sialorréia", "Sialorréia"),
        ("Desnutrição", "Desnutrição"),
        ("Astenia", "Astenia")
    )

    choices_apresenta_mucosite_se_sim = (
        ("Grau 01", "Grau 01"),
        ("Grau 02", "Grau 02"),
        ("Grau 03", "Grau 03"),
        ("Grau 04", "Grau 04")
    )

    choices_novel_consciencia = (
        ("Consciente", "Consciente"),
        ("Orientada(o)", "Orientada(o)"),
        ("Desorientada(o)", "Desorientada(o)"),
    )

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, blank=False)
    # Diagnóstico/CID
    diagnostico_cid = models.CharField(
        max_length=50, default='')

     # Sinais e/ou sintomas físicos:
    sinais_sintomas_fisicos = models.TextField(
        max_length=200, default='')

    # Tem Acompanhamento
    #  ( )Sim ( ) Não
    tem_acompanhemento = models.CharField(
        max_length=3, default='')

    # Tratamentos já realizados
    # ( ) Quimioterapia ( ) Radioterapia ( ) Cirurgia ( ) Outro
    tratamento_realizado = MultiSelectField(choices=choices_tratamento_realizado,
        max_length=50, default='')
    tratamento_realizado_out = models.TextField(max_length=200, default='')

    # Nível de Autonomia:
    # ( ) Alta Moderada ( ) Pouca ( ) Nenhuma
    nivel_autonimia = MultiSelectField(choices=choices_nivel_autonimia,max_length=50, default='')

    # Nível de consciência: ( ) Consciente ( ) Orientada(o) ( ) Desorientada(o)
    nivel_consciencia = MultiSelectField(choices=choices_novel_consciencia, max_length=50, default='')

    # História Pregressa:
    # ( ) HAS ( ) IAM( ) Sedentarismo( ) Tuberculose( ) Diabetes Mellitus ( ) Hepatites( ) Obesidade( ) AVE
    historia_progressa = MultiSelectField(choices=choices_historia_progressa,max_length=50, default='')

    # Alergias:
    # ( ) Medicamentosa ( ) Alimentar ( ) Respiratória ( ) Cutânea ( ) Outras
    alergias = MultiSelectField(choices=choices_alergias,max_length=50, default='')
    alergias_out = models.TextField(max_length=200, default='')

    # Possíveis Sinais e Sintomas Referentes a Terapia
    # ( ) Diarreia Constipação ( ) Tosse ( ) Dispnéia ( ) Palpitação ( ) Prurido ( ) Náusea ( ) Êmese ( ) Astenia ( ) Inapetência ( ) Anorexia ( ) Edema ( ) Infecção ( ) Síncope ( ) Alteração Motora ( ) Sangramento ( ) Alteração Circulatória
    possiveis_sinais_sintomas_rt = MultiSelectField(choices=choices_possiveis_sinais_sintomas_rt,max_length=50, default='')

    # Nutrição
    # ( ) Oral ( ) GTT ( ) SNE ( ) CNG
    nutricao = MultiSelectField(choices=choices_nutricao,max_length=300, default='')
    # Quatas referições realizadas
    quantas_refeicoes_realizadas = models.PositiveIntegerField(default='')

    # Possui Alguma dessas Dificuldades:
    # ( ) Dificuldade em Deglutir  ( ) Dificuldade para Mastigação ( ) Êmese ( ) Náusea
    possui_alguma_dessas_d = MultiSelectField(choices=choices_possui_alguma_dessas_d,max_length=300, default='')

    # Alteração do Paladar:
    # ( ) Sim ( ) Não se sim
    alteracao_paladar = models.CharField(max_length=3, default='')
    alteracao_paladar_se_sim = models.TextField(max_length=300, default='')

    # Qual Ingesta Hídrica Diária:
    # (   ) Água  (   ) Sucos Naturais  (   ) Sucos Industrializados  (   ) Refrigerantes  (   ) Bebidas Alcoólicas  (   ) Água de Coco
    qual_ingesta_hidrica_d = MultiSelectField(choices=choices_qual_ingesta_hidrica_d,max_length=300, default='')

    # Apresenta
    # ( ) Desidratação ( ) Sialorréia ( ) Desnutrição ( ) Astenia
    apresenta = MultiSelectField(choices=choices_apresenta, max_length=300, default='')

    # Apresenta Mucosite?
    # ( ) Sim ( ) Não se sim
    apresenta_mucosite = models.CharField(max_length=300, default='')
    apresenta_mucosite_se_sim = models.TextField(
        max_length=300, default='')

    anotacoes_adicionais = models.TextField(max_length=1000, default="")

    data_cadastro = models.DateField(default=date)

    atualizado = models.DateField(default=date)

    def __str__(self):
        return str(self.paciente) + ' - ' + str(self.paciente.usuario.nome_completo)
