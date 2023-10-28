from django.contrib import admin

from usuario.models import Usuario, Paciente

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Paciente)