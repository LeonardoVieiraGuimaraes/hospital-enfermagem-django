from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from .forms import PacienteForm, UsuarioForm
from .models import Paciente, Usuario

from django.views.decorators.csrf import ensure_csrf_cookie


# Create your views here.


######################### Views Usuario ###########################################

# class UsuarioView(TemplateView):
#     template_name = "index.html"

class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = "usuario/usuario/usuario_create.html"
    success_url = reverse_lazy('usuario.list')


    def get_success_url(self):
        return reverse_lazy('usuario.detail', kwargs={'pk': self.object.pk})


class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = "usuario/usuario/usuario_update.html"

    def get_success_url(self):
        return reverse_lazy('usuario.detail', kwargs={'pk': self.object.pk})


class UsuarioListView(ListView):
    model = Usuario
    context_object_name = 'usuarios'
    template_name = "usuario/usuario/usuario_list.html"

    def get_queryset(self):
        txt_nome = self.request.GET.get('nome_completo')

        if txt_nome:
            usuario = Usuario.objects.filter(
                nome_completo__icontains=txt_nome)

        else:
            usuario = Usuario.objects.all()

        return usuario


class UsuarioDetailView(DetailView):
    model = Usuario
    template_name = "usuario/usuario/usuario_detail.html"


class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = "usuario/usuario/usuario_delete.html"
    success_url = reverse_lazy("usuario.list")


######################### Views Paciente ###########################################

class PacienteCreateView(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = "usuario/paciente/paciente_create.html"
    success_url = reverse_lazy("paciente.detail")

    def get_success_url(self):
        return reverse_lazy('paciente.detail', kwargs={'pk': self.object.pk})


class PacientePKCreateView(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = "usuario/paciente/paciente_create.html"

    def get_initial(self):
        usuario = Usuario.objects.all()
        usuario = {'usuario': self.kwargs["pk"]}
        return usuario

    def get_success_url(self):
        return reverse_lazy('paciente.detail', kwargs={'pk': self.object.pk})


class PacienteUpdateView(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = "usuario/paciente/paciente_update.html"
    context_object_name = "paciente"

    def get_success_url(self):
        return reverse_lazy('paciente.detail', kwargs={'pk': self.object.pk})


class PacienteListView(ListView):
    model = Paciente
    context_object_name = 'pacientes'
    template_name = "usuario//paciente/paciente_list.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["pacientes"] = Paciente.objects.filter(
    #         paciente=self.kwargs.get('pk'))
    #     return context

    def get_queryset(self):
        txt_nome = self.request.GET.get('nome_completo')

        if txt_nome:
            paciente = Paciente.objects.filter(usuario__nome_completo__icontains=txt_nome)
            print(paciente)
        else:
            paciente = Paciente.objects.all()

        return paciente


class PacientePKListView(ListView):
    model = Paciente
    context_object_name = 'pacientes'
    template_name = "usuario/paciente/paciente_list.html"

    def get_queryset(self):
        qs = Paciente.objects.filter(usuario=self.kwargs.get('pk'))
        print(qs)
        return qs


class PacienteDetailView(DetailView):
    model = Paciente
    template_name = "usuario/paciente/paciente_detail.html"


class PacienteDeleteView(DeleteView):
    model = Paciente
    template_name = "usuario/paciente/paciente_delete.html"
    success_url = reverse_lazy("paciente.list")
    success_message = "Objeto Deletado"

    def get_queryset(self):
        qs = Paciente.objects.filter(questionario01=self.kwargs.get('pk'))
        print(qs)
        return qs

    # def get_error_url(self):
    #     if self.error_url:
    #         return self.error_url.format(**self.object.__dict__)
    #     else:
    #         raise ImproperlyConfigured("No error URL to redirect to. Provide a error_url.")

    # def delete(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     success_url = self.get_success_url()
    #     # error_url = self.get_error_url()

    #     try:
    #         return HttpResponseRedirect(success_url)
    #     except ProtectedError:
    #         return HttpResponseRedirect(success_url)

    # def post(self, request, *args, **kwargs):
    #     try:
    #         return self.delete(request, *args, **kwargs)
    #     except ProtectedError:
    #         messages.error(request, "custom error message")

#################################################################
# class UsuarioView(TemplateView):
#     template_name = "index.html"


# class UsuarioCreateView(CreateView):
#     model = Usuario
#     form_class = UsuarioForm
#     template_name = "usuario_create.html"

#     def get_success_url(self):
#         print(self.object.pk)
#         return reverse_lazy('usuario.editar', kwargs={'pk': self.object.pk})


# class UsuarioUpdateView(UpdateView):
#     model = Usuario
#     form_class = UsuarioForm
#     template_name = "usuario_update.html"
#     success_url = "usuario.editar"


# class UsuarioListView(ListView):
#     model = Usuario
#     context_object_name = 'usuarios'
#     template_name = "usuario_list.html"

#     def get_queryset(self):

#         txt_nome = self.request.GET.get('nome_completo')

#         if txt_nome:
#             usuario = Usuario.objects.filter(
#                 nome_completo__icontains=txt_nome)

#         else:
#             usuario = Usuario.objects.all()

#         return usuario


# class UsuarioDetailView(DetailView):
#     model = Usuario
#     template_name = "usuario_detail.html"


# ######################### Views Paciente ###########################################


# # class PacienteCreateView(CreateView):
# #     model = Paciente
# #     form_class = PacienteForm
# #     # success_url = "paciente.editar"

# #     def get_success_url(self):
# #         print(self.object.pk)
# #         return reverse_lazy('paciente.editar', kwargs={'pk': self.object.pk})


# # class PacienteUpdateView(UpdateView):
# #     model = Paciente
# #     form_class = PacienteForm

# #     success_url = "paciente.editar"


# # class PacienteListView(ListView):
# #     model = Paciente
# #     context_object_name = 'pacientes'

# #     def get_queryset(self):

# #         txt_nome = self.request.GET.get('nome_completo')

# #         if txt_nome:
# #             usuario = Paciente.objects.filter(
# #                 nome_completo__icontains=txt_nome)

# #         else:
# #             usuario = Paciente.objects.all()

# #         return usuario


# # class PacienteDetailView(DetailView):
# #     model = Paciente

# #     def get_success_url(self):
# #         print(self.object.pk)
# #         return reverse_lazy('questionario0101.listar', kwargs={'pk': self.object.pk})


# # class UsuarioCreateView(CreateView):
# #     model = Usuario
# #     form_class = UsuarioForm
# #     # success_url = "/usuario/editar"

# #     # def get_success_url(self):
# #     #     print(self.object.pk)
# #     #     return reverse_lazy('usuario.detalhar', kwargs={'pk': self.object.pk})

# #     def get_success_url(self):
# #         print(self.object.pk)
# #         return reverse_lazy('usuario.editar', kwargs={'pk': self.object.pk})


# # class UsuarioListView(ListView):
# #     model = Usuario
# #     context_object_name = 'usuarios'

# #     def get_queryset(self):

# #         txt_nome = self.request.GET.get('nome_completo')

# #         if txt_nome:
# #             usuario = Usuario.objects.filter(
# #                 nome_completo__icontains=txt_nome)

# #         else:
# #             usuario = Usuario.objects.all()

# #         return usuario


# # class UsuarioUpdateView(UpdateView):
# #     model = Usuario
# #     form_class = UsuarioForm

# #     success_url = "/usuario/listar"


# # class UsuarioDetailView(DetailView):
# #     model = Usuario


# # class UsuarioDeleteView(DeleteView):
# #     model = Usuario

# #     success_url = "/usuario/listar"
