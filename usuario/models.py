from datetime import date, datetime

from cpf_field.models import CPFField
from django.db import models


# from questionario.models import Questionario0101


# Create your models here.

####################################### Model Pessoa Física #################################

class Usuario(models.Model):
    date = str(date.today())
    datenow = datetime.now()
    # id = models.IntegerField(primary_key=True)
    cpf = CPFField(default='', unique=True)
    nome_completo = models.CharField(max_length=100, default='')
    data_nascimento = models.DateField(date)
    idade = models.IntegerField(default=0)
    reside_em = models.CharField(max_length=100, default='')
    telefone = models.CharField(max_length=20, default='')
    nome_mae = models.CharField(max_length=100, default='')
    nome_pai = models.CharField(max_length=100, default='')
    reg = models.CharField(max_length=100, default='')

    data_cadastro = models.DateField(default='date')
    atualizado = models.DateField(default='date')

    def __str__(self):
        return str(self.cpf) + ' - ' + self.nome_completo


####################################### Model Paciente  #################################


class Paciente(models.Model):
    date = str(date.today())
    datenow = datetime.now()

    usuario = models.OneToOneField(
        Usuario, on_delete=models.CASCADE, default="")

    prontuario = models.CharField(max_length=50, default='', unique=True)

    data_cadastro = models.DateField(default='date')
    atualizado = models.DateField(default='date', )

    def __str__(self):
        return str(self.usuario)


####################################### Model Paciente  #################################


class Colaborador(models.Model):
    date = str(date.today())
    datenow = datetime.now()

    usuario = models.OneToOneField(
        Usuario, on_delete=models.CASCADE, default="")
    funcao = models.CharField(max_length=20, default='')
    carteria_trabalho = models.CharField(max_length=50, default='')

    data_cadastro = models.DateField(date)
    atualizado = models.DateField(date)

    def __str__(self):
        return str(self.usuario)
