from datetime import date, datetime

from django import forms

from usuario.models import Paciente
from .models import Questionario01, Questionario0101, Questionario0102, Questionario02, Questionario0103


#   # CIRURGIA PROPOSTA
# cirurgia_proposta = forms.CharField()

# # Sala Cirurgica:
# sala_cirugica = forms.CharField()

# # Data da Cirurgia:
# data_cirurugia = forms.DateField()
# # Modalidade ( ) Eletiva (  )Urgência ( )Emergência
# modalidade = forms.CharField()

# # COMORBIDADE
# comorbidade = forms.CharField()

# •	DADOS DO USUÁRIO:
# USUARIO:
# DATA DE NASCIMENTO
# PRONTUÁRIO:
# NOME DA MAE:
# CIRURGIA PROPOSTA:
#  DATA DA CIRURGIA
# SALA DE CIRURGIA:
# COMORBIDADE:
# MODALIDADE: (  )ELETIVA (  )URGÊNCIA ( ) EMEREGENCIA

##################################### Cirurgia #######################################


class Questionario01Form(forms.ModelForm):
    choices_modalidade = (
        ("Eletiva", "Eletiva"),
        ("Urgência", "Urgência"),
        ("Emergência", "Emergência"),
    )
    paciente = forms.ModelChoiceField(queryset=Paciente.objects.all(), label="Paciente", widget=forms.Select())

    # paciente = forms.ModelChoiceField(
    #     queryset=Paciente.objects.all(), label="Paciente", widget=forms.Select())

    # CIRURGIA PROPOSTA
    cirurgia_proposta = forms.CharField()

    # Sala Cirurgica:
    sala_cirurgica = forms.CharField(label="Sala Cirurgica")

    # Data da Cirurgia:
    data_cirurgia = forms.DateField(widget=forms.DateInput(
        format='%Y-%m-%d', attrs={"type": 'date'}))
    # Modalidade ( ) Eletiva (  )Urgência ( )Emergência
    modalidade = forms.ChoiceField(
        required=False, choices=choices_modalidade, widget=forms.RadioSelect())

    # COMORBIDADE
    comorbidade = forms.CharField()

    data_cadastro = forms.DateField(widget=forms.DateInput(
        format='%Y-%m-%d', attrs={"type": 'date', 'readonly': 'readonly'}), initial=date.today())

    atualizado = forms.DateField(widget=forms.DateInput(
        format='%Y-%m-%d', attrs={"type": 'date', 'readonly': 'readonly'}), initial=date.today())

    class Meta:
        model = Questionario01
        fields = "__all__"


# ENTRADA ANTES DA INDUÇÃO ANESTESISCA


class Questionario0101Form(forms.ModelForm):
    choices_triconomia_qual_meio = (
        ("Aparador", "Aparador"),
        ("Barbeador", "Barbeador")
    )

    choices_triconomia_local = (
        ("Bloco cirúrgico", "Bloco cirúrgico"),
        (" Clinica", " Clinica")
    )

    choices_sn = (
        ("Sim", "Sim"),
        ("Não", "Não"),
    )

    choices_sna = (
        ("Sim", "Sim"),
        ("Não", "Não"),
        ("NA", "NA"),
    )

    # Retonorna o prontuário
    cirurgia_segura = forms.ModelChoiceField(queryset=Questionario01.objects.all(
    ), label="Paciente:", widget=forms.Select())

    # Pulseira de identificação  ( ) S  (  ) N
    pulseira_identificacao = forms.ChoiceField(widget=forms.RadioSelect(
    ), choices=choices_sn, label="Pulseira de identificação:")

    #   PRONTUARIO COMPLETO:  (   ) SIM (   ) NÃO
    # QUAIS DOCUMENTOS FALTAM:-------------------------

    prontuario_completo = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={'onClick':'radioOcultar(this)'}), choices=choices_sn, label="Prontuário Completo:")
    prontuario_completo_se_nao = forms.CharField(required=False,label="Se não, Quais documentos faltam:", widget=forms.TextInput())

    #  POSSUI  DISPOSITIVOS : (  ) SIM   (  ) NÃO
    # QUAIS ? -------------------------------------------------

    possui_dispositivos = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={'onClick':'radioOcultar(this)'}), choices=choices_sn, label="Possui dispositivos:")
    possui_dispositivos_se_sim = forms.CharField(required=False,
        label="Se sim, quais:", widget=forms.TextInput())

    # PROCEDIEMNTOS CONFIRMADO: (  ) SIM (  ) NÃO
    procedimento_confirmado = forms.ChoiceField(
        widget=forms.RadioSelect(), choices=choices_sn, label="Procedimento confirmado")

    # Termo de Consentimento Cirúrgico e Anestésico: () sim() não
    termo_consentimento_c_a = forms.ChoiceField(
        widget=forms.RadioSelect(), choices=choices_sn, label="Termo de consentimento cirúrgico e anestésico:")

    #  EXAMES DE IMAGEM DISPONIVEIS: (  ) SIM (  ) NÃO
    exames_laborat_i_d = forms.ChoiceField(
        widget=forms.RadioSelect(), choices=choices_sn, label="Exame: Laborat. Imagens disponível:")

    # RISCO DE PERDA SANGUINEA+ 500ML:  (  ) SIM (  ) NÃO
    risco_perda_s = forms.ChoiceField(
        widget=forms.RadioSelect(), choices=choices_sn, label="Risco de perda sanguínea + 500ml:")

    # RESSERVA DE HEMODERIVADOS:  (  ) SIM (  ) NÃO
    resserva_hemoderivados = forms.ChoiceField(
        widget=forms.RadioSelect(), choices=choices_sn, label="Reserva de homoderivados:")

    # Reserva de CTI: () sim() não
    resserva_CTI = forms.ChoiceField(
        widget=forms.RadioSelect(), choices=choices_sn, label="Reserva de CTI:")

    # SITIO CIRURGICO DEMARCADO:  (  ) SIM (  ) NÃO
    sitio_cirurgico_d = forms.ChoiceField(
        widget=forms.RadioSelect(), choices=choices_sn, label="Sitio cirúrgico demarcado:")

    # Jejum ( ) S - inicio ______ ( )  N
    jejum = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={'onClick':'radioOcultar(this)'}), choices=choices_sn, label="Jejum:")
    jejum_se_sim = forms.TimeField(required=False,widget=forms.TimeInput(attrs={"type": 'time'}),
                                   label="Se sim, hora:")

    # Alergia conhecida: : ( ) sim ( ) não / Se sim Qual?
    alergia_conhecida = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={'onClick':'radioOcultar(this)'}), choices=choices_sna, label="Alergia Conhecia:")
    alergia_conhecida_se_sim = forms.CharField(required=False, label="Se sim, qual?", widget=forms.TextInput())

    # TRICOTOMIA: (  ) SIM (  ) NÃO (  )  NA ,
    # HORA: -------
    # QUAL MEIO: (  ) APARADOR  (  ) BARBEADOR
    # LOCAL: (  ) BLOCO CIRURGICO  (  ) CLINICA

    triconomia_realizada = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={'onClick':'radioOcultar(this)'}), choices=choices_sna, label="Tricotomia:")
    triconomia_realizada_se_sim_01 = forms.TimeField(
        required=False, widget=forms.TimeInput(attrs={"type": 'time'}), label="Se sim, hora:")
    triconomia_realizada_se_sim_02 = forms.ChoiceField(required=False,
        widget=forms.RadioSelect(), choices=choices_triconomia_qual_meio, label="Qual meio:")
    triconomia_realizada_se_sim_03 = forms.ChoiceField(required=False,
        widget=forms.RadioSelect(), choices=choices_triconomia_local, label="Local:")

    # Relizou Quimeoterapia : ( ) N ( ) S Quantas sessões ___ ultima sessão
    realizou_quimeoterapia = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={'onClick':'radioOcultar(this)'}), choices=choices_sn, label="Relizou Quimeoterapia:")

    realizou_quimeoterapia_se_sim_01 = forms.IntegerField(required=False, label="Quantas Sessões:", widget=forms.NumberInput())

    realizou_quimeoterapia_se_sim_02 = forms.DateField(required=False, widget=forms.DateInput(format='%Y-%m-%d',attrs={"type": 'date'}),initial=date.today(), label="Ultima Sessão:")

    # Realizou Radioterapia: ( ) N ( ) S Quantas sessões ___ ultima sessão
    realizou_radioterapia = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={'onClick':'radioOcultar(this)'}), choices=choices_sn, label="Relizou Radioterapia:")

    realizou_radioterapia_se_sim_01 = forms.IntegerField(required=False, widget=forms.NumberInput(),
        label="Quantas Sessões:")

    realizou_radioterapia_se_sim_02 = forms.DateField(required=False, widget=forms.DateInput(
        format='%Y-%m-%d', attrs={"type": 'date'}), initial=date.today(),label="Ultima Sessão:")

    #     REALIZOU HEMODIALISE: (  ) SIM (  ) NÃO
    # QUANTAS SESSÕES:
    # ULTIMA SESSÃO:

    realizou_hemodialise = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={'onClick':'radioOcultar(this)'}), choices=choices_sn, label="Relizou Hemodialise:")

    realizou_hemodialise_se_sim_01 = forms.IntegerField(
        required=False, label="Quantas Sessões:")

    realizou_hemodialise_se_sim_02 = forms.DateField(required=False, widget=forms.DateInput(
        format='%Y-%m-%d', attrs={"type": 'date', 'readonly': 'readonly'}), initial=date.today(),
                                                     label="Ultima Sessão:")

    # REALIZOU TRANSPLANTE DE ÓRGAO: (  ) SIM  (  ) NÃO
    # QUAL ANO: ----------
    realizou_transplante_o = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={'onClick':'radioOcultar(this)'}), choices=choices_sn, label="Realizou transplante de órgão:")
    realizou_transplante_o_se_sim = forms.IntegerField(
        required=False, label="Qual ano:")

    # Verificação Anestésica: Materiais VAD, Medicações e Equipamentos adequados:
    # () sim() não / Se Não Qual?

    verificacao_anestesica_m_v_m_e_a = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={'onClick':'radioOcultar(this)'}), choices=choices_sn,
        label="Verificação Anestésica: Materiais VAD, Medicações e Equipamentos adequados:")
    verificacao_anestesica_m_v_m_e_a_se_nao = forms.IntegerField(
        required=False, label="Se não, qual ano:")

    # Vias Aéreas difíceis ou risco de Aspiração: () sim() não
    vias_aereas_d_r_a = forms.ChoiceField(
        widget=forms.RadioSelect(), choices=choices_sn, label="Vias Aéreas difíceis ou risco de Aspiração:")

    # Tempo previsto para cirurgia() sim() não
    tempo_previsto_cirurgia = forms.ChoiceField(
        widget=forms.RadioSelect(), choices=choices_sn, label="Tempo previsto para cirurgia:")

    data_cadastro = forms.DateField(widget=forms.DateInput(
        format='%Y-%m-%d', attrs={"type": 'date', 'readonly': 'readonly'}), initial=date.today())

    atualizado = forms.DateField(widget=forms.DateInput(
        format='%Y-%m-%d', attrs={"type": 'date', 'readonly': 'readonly'}), initial=date.today())

    # def clean_realizou_quimeoterapia_se_sim_01(self):
    #     clean = self.cleaned_data['realizou_quimeoterapia_se_sim_01']
    #     if clean > 100:
    #         raise forms.ValidationError("maior que 100")
    #     return clean

    class Meta:
        model = Questionario0101
        fields = "__all__"


class Questionario0102Form(forms.ModelForm):
    choices_sn = (
        ("Sim", "Sim"),
        ("Não", "Não"),
    )
    choices_sna = (
        ("Sim", "Sim"),
        ("Não", "Não"),
        ("NA", "NA"),
    )

    cirurgia_segura = forms.ModelChoiceField(queryset=Questionario01.objects.all(
    ), label="Paciente:", widget=forms.Select())

    #  TODOS OS MEMBROS DA EQUIPE ESTÃO PRESENTES: (  ) SIM (  ) NÃO
    todos_membros_e_e_p = forms.ChoiceField(
        widget=forms.RadioSelect(), choices=choices_sn, label="Todos os membros da equipe estão presentes:")
    # TODOS CONFIRMAM NOVAMENTE :
    # NOME DO PACIENTE  (  ) SIM ( ) NÃO
    nome_paciente = forms.ChoiceField(
        widget=forms.RadioSelect(), choices=choices_sn, label="Nome do paciente")

    # SITITO CIRURGICO:  (  ) SIM (  ) NÃO
    sitio_cirurgico = forms.ChoiceField(
        widget=forms.RadioSelect(), choices=choices_sn, label="Sitio cirurgico:")

    # PROCEDIMENTO;  (  ) SIM (  ) NÃO
    procedimento = forms.ChoiceField(
        widget=forms.RadioSelect(), choices=choices_sn, label="Procedimento:")

    # LATERALIDADE:  (  ) SIM (  ) NÃO
    lateralidade = forms.ChoiceField(
        widget=forms.RadioSelect(), choices=choices_sn, label="Lateralidade:")

    # ANTE ASSEPSIA DO CAMPO OPERATÓRIO:  (  ) SIM (  ) NÃO
    # SE SIM QUAL O PRODUTO?
    antes_assepsia_c_o = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={'onClick':'radioOcultar(this)'}), choices=choices_sn, label="Ante assepsia do campo operatório:")
    antes_assepsia_c_o_se_sim = forms.CharField(required=False, label="Se sim, qual o produto")

    # O ANTIBIOTICO PROFILÁTICO FOI ADMINISTRADO NOS ULTIMOS 60 MINUTOS:   (  ) SIM  (  ) NÃO ( ) Na
    # se sim, hora:

    antibiotico_profilatico_a_u_m = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={'onClick':'radioOcultar(this)'}), choices=choices_sna,
        label="O antibiotico profilático foi administrado nos último 60 minutos:")
    antibiotico_profilatico_a_u_m_se_sim_01 = forms.TimeField(required=False, widget=forms.TimeInput(
        attrs={"type": 'time'}), label="Se sim, hora")

    # Hora da Incisão cirúrgica: _________
    hora_incisao_c = forms.TimeField(widget=forms.TimeInput(
        attrs={"type": 'time'}), label="Hora da Incisão Cirúrgica")

    # Placa de bisturi posicionado? ( ) sim() não() NA
    placa_bisturi_p = forms.ChoiceField(
        widget=forms.RadioSelect(), choices=choices_sna,
        label="Placa de bisturi posicionado:")

    # Materiais e instrumentais conferidos e disponível: ( ) sim ( ) não Se sim, quais? _______

    materiais_instumentais_c_d = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={'onClick':'radioOcultar(this)'}), choices=choices_sna,
        label="Materiais e instrumentais conferidos e disponível:")
    materiais_instumentais_c_d_se_sim_01 = forms.CharField(required=False,label="Se sim, quais?")

    # fita indicadora química do material: ( ) sim ( )não
    fita_indicador_q_m = forms.ChoiceField(
        widget=forms.RadioSelect(), choices=choices_sn,
        label="Fita indicadora química do material:")

    # integrador do material: ( ) sim ( ) não
    integrador_material = forms.ChoiceField(
        widget=forms.RadioSelect(), choices=choices_sn,
        label="Integrador do material")

    # Data do vencimento
    data_vencimento = forms.DateField(widget=forms.DateInput(
        format='%Y-%m-%d', attrs={"type": 'date'}))

    # cirurgia realizada ___________________
    cirurgia_realizada = forms.CharField(label="Cirurgia realizada")

    # # Registro completo e peças registradas no livro de procedimento ( ) sim ( ) não
    # registro_completo_p_r_l_p = forms.ChoiceField(
    #     widget=forms.RadioSelect(), choices=choices_sn,
    #     label="Registro completo e peças registradas no livro de procedimento")

    data_cadastro = forms.DateField(widget=forms.DateInput(
        format='%Y-%m-%d', attrs={"type": 'date', 'readonly': 'readonly'}), initial=date.today())

    atualizado = forms.DateField(widget=forms.DateInput(
        format='%Y-%m-%d', attrs={"type": 'date', 'readonly': 'readonly'}), initial=date.today())

    class Meta:
        model = Questionario0102
        fields = "__all__"


class Questionario0103Form(forms.ModelForm):
    date = str(date.today())
    datenow = datetime.now()
    time = f"{datenow.hour}:{datenow.minute}"

    choices_sn = (
        ("Sim", "Sim"),
        ("Não", "Não"),
    )

    choices_alta_confirmada = (
        ("RPAn", "RPAn"),
        ("CTI", "CTI"),
        ("ENFERMARIA", "ENFERMARIA"),
        ("ÒBITO", "ÒBITO"),
    )

    cirurgia_segura = forms.ModelChoiceField(queryset=Questionario01.objects.all(
    ), label="Paciente:", widget=forms.Select())
    ###########################################################
    # CONTAGEM :
    # INSTRUMENTAIS  : ANTES :  --------  DEPOIS --------

    # COMPRESSAS:   ANTES :  -------- DEPOIS --------
    # AGULHAS  : ANTES :  ------ DEPOIS --------
    # Lâmina de Bisturi : Antes: _______ Depois: _____________
    instrumentais_antes = forms.IntegerField()
    compressas_antes = forms.IntegerField()
    agulhas_antes = forms.IntegerField()
    lamina_bisturi_antes = forms.IntegerField()

    instrumentais_depois = forms.IntegerField()
    compressas_depois = forms.IntegerField()
    agulhas_depois = forms.IntegerField()
    lamina_bisturi_depois = forms.IntegerField()

    # CIRÚRGIA REALIZADA: -----------------------------------
    cirurgia_realizada = forms.CharField(label='Cirúrgia Realizada:')

    # REGISTRO COMPLETO DO PROCEDIMENTO  E PEÇAS NO LIVRO DE PROCEDIMENTO (  ) SIM (  ) NÃO
    registro_completo_p_p_l_p = forms.ChoiceField(
        widget=forms.RadioSelect(), choices=choices_sn,
        label="Registro completo do procedimento e peças registradas no livro de procedimento:")

    # HOUVE ALGUM PROBLEMA COM MATERIAIS, EQUIPAMENTOS E INSTRUMENTOS : (  )SIM (  )NÃO
    houve_algum_p_m_e_i = forms.ChoiceField(
        widget=forms.RadioSelect(), choices=choices_sn,
        label="Houve algum problema com matériais, equipamentos e instrumentos:")

    # PEÇA PATOLOGICA: (  ) SIM (  ) NÃO
    peca_patologica = forms.ChoiceField(
        widget=forms.RadioSelect(), choices=choices_sn,
        label="Peça Patologica:")

    # AMOSTRA DE CULTURA: (  ) SIM (  ) NÃO
    amostra_cultura = forms.ChoiceField(
        widget=forms.RadioSelect(), choices=choices_sn,
        label="Amostra de Cultura:")

    # CITOLOGIA ONCOTICA: (  ) SIM  (  ) NÃO
    citologia_oncotica = forms.ChoiceField(
        widget=forms.RadioSelect(), choices=choices_sn,
        label="Citologia oncotica:")
    # AMOSTRA DE  LCR: líquido cefalorraquidiano (  ) SIM (  ) NÃO
    amostra_lcr = forms.ChoiceField(
        widget=forms.RadioSelect(), choices=choices_sn,
        label="Amostra de LCR: liquido cefalorraquidiano:")

    #############################################################
    # CIÚRGIÃO, ANESTESISTA E ENFERMAGEM CONFIMAM
    # ALTA CONFIRMADA : (  ) RPAn(   ) CTI (  ) ENFERMARIA (  )ÒBITO

    alta_confirmada = forms.ChoiceField(
        widget=forms.RadioSelect(), choices=choices_alta_confirmada,
        label="Alta Confirmada")

    # OBSERVAÇÕES: --------------------------------------------------------------------
    observacoes = forms.CharField(label="Observações")

    # Cirurgião _______________________
    cirurgiao = forms.CharField(label="Cirurgião")

    # Anestesista _______________________
    anestesista = forms.CharField(label="Anestesista")
    # Enfermeiro _______________________
    enfermeiro = forms.CharField(label="Enfermeiro")
    # Circulante_______________________
    circulante = forms.CharField(label="Circulante")

    data_cadastro = forms.DateField(widget=forms.DateInput(
        format='%Y-%m-%d', attrs={"type": 'date', 'readonly': 'readonly'}), initial=date)

    atualizado = forms.DateField(widget=forms.DateInput(
        format='%Y-%m-%d', attrs={"type": 'date', 'readonly': 'readonly'}), initial=date)

    class Meta:
        model = Questionario0103
        fields = "__all__"


####################### Questionário 02 ##########################
class Questionario02Form(forms.ModelForm):
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

    paciente = forms.ModelChoiceField(
        queryset=Paciente.objects.all(), label="Paciente    ", widget=forms.Select())

    # Diagnóstico/CID
    diagnostico_cid = forms.CharField(label="Diagnóstico/CID:")

    # Sinais e/ou sintomas físicos:
    sinais_sintomas_fisicos = forms.CharField(widget=forms.Textarea(),
        label="Sinais e/ou sintomas físicos:")

    # Tem Acompanhamento
    #  ( )Sim ( ) Não
    tem_acompanhemento = forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=choices_sn, label="Tem Acompanhamento")

    # Tratamentos já realizados
    # ( ) Quimioterapia ( ) Radioterapia ( ) Cirurgia ( ) Outro
    tratamento_realizado = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(attrs={'onClick':'CheckBoxOcultar(this)'}),
        choices=choices_tratamento_realizado, label="Tratamentos já realizados:")
    tratamento_realizado_out = forms.CharField(required=False,
                                               widget=forms.Textarea(attrs={'disabled':'disabled'}), label="")

    # Nível de Autonomia:
    # ( ) Alta Moderada ( ) Pouca ( ) Nenhuma
    nivel_autonimia = forms.ChoiceField(
        widget=forms.RadioSelect(), choices=choices_nivel_autonimia, label="Nível de Autonomia:")

    # Nível de consciência: ( ) Consciente ( ) Orientada(o) ( ) Desorientada(o)

    nivel_consciencia = forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=choices_novel_consciencia, label="Nivel de Consciência")


    # História Pregressa:
    # ( ) HAS ( ) IAM( ) Sedentarismo( ) Tuberculose( ) Diabetes Mellitus ( ) Hepatites( ) Obesidade( ) AVE
    historia_progressa = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=choices_historia_progressa, label="História Pregressa:")

    # Alergias:
    # ( ) Medicamentosa ( ) Alimentar ( ) Respiratória ( ) Cutânea ( ) Outras
    alergias = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(attrs={'onClick':'CheckBoxOcultar(this)'}),
        choices=choices_alergias, label="Alergias:")
    alergias_out = forms.CharField(widget=forms.Textarea(attrs={"disabled":"disabled"}
        ), label="")

    # Possíveis Sinais e Sintomas Referentes a Terapia
    # ( ) Diarreia Constipação ( ) Tosse ( ) Dispnéia ( ) Palpitação ( ) Prurido ( ) Náusea ( ) Êmese ( ) Astenia ( ) Inapetência ( ) Anorexia ( ) Edema ( ) Infecção ( ) Síncope ( ) Alteração Motora ( ) Sangramento ( ) Alteração Circulatória
    possiveis_sinais_sintomas_rt = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(),choices=choices_possiveis_sinais_sintomas_rt,
        label="Possíveis Sinais e Sintomas Referentes a Terapia:")

    # Nutrição
    # ( ) Oral ( ) GTT ( ) SNE ( ) CNG
    nutricao = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=choices_nutricao, label="Nutrição")
    quantas_refeicoes_realizadas = forms.IntegerField(
        label="Quantas refeições realizadas no dia?")

    # Possui Alguma dessas Dificuldades:
    # ( ) Dificuldade em Deglutir  ( ) Dificuldade para Mastigação ( ) Êmese ( ) Náusea
    possui_alguma_dessas_d = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=choices_possui_alguma_dessas_d, label="Possui Alguma dessas Dificuldades:")

    # Alteração do Paladar:
    # ( ) Sim ( ) Não
    alteracao_paladar = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={'onClick':'radioOcultar(this)'}),
        choices=choices_sn, label="Alteração do Paladar:")
    alteracao_paladar_se_sim = forms.CharField(required=False,
                                               label="Se sim, qual:",
                                               widget=forms.TextInput())

    # Qual Ingesta Hídrica Diária:
    # (   ) Água  (   ) Sucos Naturais  (   ) Sucos Industrializados  (   ) Refrigerantes  (   ) Bebidas Alcoólicas  (   ) Água de Coco
    qual_ingesta_hidrica_d = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(),choices=choices_qual_ingesta_hidrica_d, label="Qual Ingesta Hídrica Diária:")

    # Apresenta
    # ( ) Desidratação ( ) Sialorréia ( ) Desnutrição ( ) Astenia
    apresenta = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=choices_apresenta, label="Apresenta")

    # Apresenta Mucosite?
    # ( ) Sim ( ) Não
    apresenta_mucosite = forms.ChoiceField(widget=forms.RadioSelect(attrs={'onClick':'radioOcultar(this)'}), choices=choices_sn, label="Apresenta Mucosite?")
    apresenta_mucosite_se_sim = forms.ChoiceField(required=False,
                                                  widget=forms.RadioSelect(
                                                     ),
                                                  choices=choices_apresenta_mucosite_se_sim, label="Se Sim:")

    anotacoes_adicionais = forms.CharField(widget=forms.Textarea())

    # Data cadastro
    data_cadastro = forms.DateField(widget=forms.DateInput(
        format='%Y-%m-%d', attrs={"type": 'date', 'readonly': 'readonly'}), initial=date)

    atualizado = forms.DateField(widget=forms.DateInput(
        format='%Y-%m-%d', attrs={"type": 'date', 'readonly': 'readonly'}), initial=date)

    class Meta:
        model = Questionario02
        fields = "__all__"
