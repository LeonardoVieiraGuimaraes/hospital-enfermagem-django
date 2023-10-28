from datetime import date

from django import forms

from .models import Usuario, Paciente


################################################# Forms Usuario ######################
class UsuarioForm(forms.ModelForm):
    date = str(date.today())
    cpf = forms.CharField(label="CPF")

    nome_completo = forms.CharField(label="Nome Completo")

    data_nascimento = forms.DateField(label="Data de Nascimento", widget=forms.DateInput(
        format='%Y-%m-%d', attrs={"type": 'date'}))

    idade = forms.IntegerField(label="Idade")

    reside_em = forms.CharField(label="Endereço")

    telefone = forms.CharField(label="Telefone")

    nome_mae = forms.CharField(label="Nome da Mãe")
    nome_pai = forms.CharField(label="Nome do Pai", required=False)

    data_cadastro = forms.DateField(required=False, widget=forms.DateInput(
        format='%Y-%m-%d', attrs={"type": 'date', 'readonly': 'readonly', 'value': date}), initial=date)

    atualizado = forms.DateField(required=False, widget=forms.DateInput(
        format='%Y-%m-%d', attrs={"type": 'date', 'value': date}), initial=date)

    class Meta:
        model = Usuario
        fields = "__all__"


################################################# Forms Paciente ######################

class PacienteForm(forms.ModelForm):
    date = str(date.today())

    # USUÁRIO

    usuario = forms.ModelChoiceField(
        queryset=Usuario.objects.all(), label="Usuario", widget=forms.Select())
    # PRONTUÁRIO

    prontuario = forms.CharField(label="Prontuário")

    data_cadastro = forms.DateField(required=False, widget=forms.DateInput(
        format='%Y-%m-%d', attrs={"type": 'date', 'readonly': 'readonly', 'value': date}),
                                    initial=date)

    atualizado = forms.DateField(required=False, widget=forms.DateInput(
        format='%Y-%m-%d', attrs={"type": 'date', 'readonly': 'readonly'}), initial=date)

    class Meta:
        model = Paciente
        fields = "__all__"

#####################################################################

# # CIRURGIA PROPOSTA
# cirurgia_proposta = forms.CharField()

# # Sala Cirurgica:
# sala_cirugica = forms.CharField()

# # Data da Cirurgia:
# data_cirurugia = forms.DateField()
# # Modalidade ( ) Eletiva (  )Urgência ( )Emergência
# modalidade = forms.CharField()

# # COMORBIDADE
# comorbidade = forms.CharField()
# class UsuarioForm(forms.ModelForm):

#     # data_nascimento = forms.DateField(widget=forms.DateInput(
#     #     format='%Y-%m-%d', attrs={"type": 'date'}))

#     # data_cadastro = forms.DateField(widget=forms.DateInput(
#     #     format='%Y-%m-%d', attrs={"type": 'date', 'readonly': 'readonly'}), initial=date.today())

#     # cpf = forms.CharField(label="CPF")

#     # nome_mae = forms.CharField(label="Nome da Mãe")
#     # nome_pai = forms.CharField(label="Nome do Pai", required=False)

#     class Meta:
#         model = Usuario
#         fields = "__all__"


# # class PacienteForm(UsuarioForm):

# #     # data_nascimento = forms.DateField(widget=forms.DateInput(
# #     #     format='%Y-%m-%d', attrs={"type": 'date'}))

# #     # data_cadastro = forms.DateField(widget=forms.DateInput(
# #     #     format='%Y-%m-%d', attrs={"type": 'date', 'readonly': 'readonly'}), initial=date.today())

# #     # cpf = forms.CharField(label="CPF")

# #     # nome_mae = forms.CharField(label="Nome da Mãe")
# #     # nome_pai = forms.CharField(label="Nome do Pai", required=False)

# #     # USUÁRIO
# #     # DATA NASCIMENTO
# #     # NOME DA MÃE
# #     # usuario = forms.ModelChoiceField(queryset = Usuario.objects.all(), label = "Usuario", widget = forms.Select())
# #     # PRONTUÁRIO
# #     # prontuario = forms.CharField()

# #     # # CIRURGIA PROPOSTA
# #     # cirurgia_proposta = forms.CharField()

# #     # # Sala Cirurgica:
# #     # sala_cirugica = forms.CharField()

# #     # # Data da Cirurgia:
# #     # data_cirurugia = forms.DateField()
# #     # # Modalidade ( ) Eletiva (  )Urgência ( )Emergência
# #     # modalidade = forms.CharField()

# #     # # COMORBIDADE
# #     # comorbidade = forms.CharField()

# #     # data_cadastro = forms.DateField(widget=forms.DateInput(
# #     #     format='%Y-%m-%d', attrs={"type": 'date', 'readonly': 'readonly'}), initial=date.today())

# #     class Meta:
# #         model = Paciente
# #         fields = "__all__"
