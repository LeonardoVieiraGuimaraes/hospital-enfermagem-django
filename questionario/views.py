from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from usuario.models import Paciente
from .forms import Questionario0101Form, Questionario01Form, Questionario0102Form, Questionario0103Form, \
    Questionario02Form
from .models import Questionario01, Questionario0101, Questionario0102, Questionario0103, Questionario02


# Create your views here.


########################################## Questionario Cirurgia ##########################


# class QuestionarioView(TemplateView):
#     template_name = "main/index.html"

class Questionario01CreateView(CreateView):
    form_class = Questionario01Form
    model = Questionario01
    template_name = "questionario/questionario01/questionario01_create.html"

    # success_url = reverse_lazy('questionario01.detail')

    def get_success_url(self):
        print(self.object.pk)
        return reverse_lazy('questionario01.detail', kwargs={'pk': self.object.pk})


class Questionario01PKCreateView(CreateView):
    form_class = Questionario01Form
    model = Questionario01
    template_name = "questionario/questionario01/questionario01_create.html"

    def get_success_url(self):
        print(self.object.pk)
        return reverse_lazy('questionario01.detail', kwargs={'pk': self.object.pk})

    def get_initial(self):
        pacientes = Paciente.objects.all()
        print(pacientes)
        return {'paciente': self.kwargs["pk"]}


class Questionario01DetailView(DetailView):
    model = Questionario01
    template_name = "questionario/questionario01/questionario01_detail.html"
    # context_object_name = "questionario01"

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     # context['questionarios0101'] = Questionario0101.objects.all()
    #
    #     context["questionarios0101"] = Questionario0101.objects.filter(
    #         cirurgia_segura_id=self.kwargs.get('pk'))
    #     return context


class Questionario01ListView(ListView):
    model = Questionario01
    template_name = "questionario/questionario01/questionario01_list.html"
    context_object_name = 'questionarios01'

    def get_queryset(self):
        txt_nome = self.request.GET.get('nome_completo')

        if txt_nome:
            usuario = Questionario01.objects.filter(
                paciente__usuario__nome_completo__icontains=txt_nome)

        else:
            usuario = Questionario01.objects.all()

        return usuario


class Questionario01PKListView(ListView):
    model = Questionario01
    template_name = "questionario/questionario01/questionario01pk_list.html"
    context_object_name = 'questionarios01'

    def get_queryset(self):
        qs = Questionario01.objects.filter(paciente=self.kwargs.get('pk'))
        print(qs)
        return qs

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["questionarios01pk"] = Questionario01.objects.filter(
    #         paciente=self.kwargs.get('pk'))
    #     return context


class Questionario01UpdateView(UpdateView):
    model = Questionario01
    form_class = Questionario01Form
    template_name = "questionario/questionario01/questionario01_update.html"

    def get_success_url(self):
        return reverse_lazy('questionario01.detail', kwargs={'pk': self.object.pk})


class Questionario01DeleteView(DeleteView):
    model = Questionario01
    template_name = "questionario/questionario01/questionario01_delete.html"


########################################## Questionario Cirurgia Entrada ##########################

class Questionario0101PKCreateView(CreateView):
    form_class = Questionario0101Form
    model = Questionario0101
    template_name = "questionario/questionario01/questionario0101/questionario0101_create.html"

    def get_initial(self):
        cirurgia_segura = {'cirurgia_segura': self.kwargs["pk"]}
        return cirurgia_segura

    def get_success_url(self):
        return reverse_lazy('questionario01.detail', kwargs={'pk': self.object.cirurgia_segura_id})


class Questionario0101UpdateView(UpdateView):
    model = Questionario0101
    form_class = Questionario0101Form
    template_name = "questionario/questionario01/questionario0101/questionario0101_update.html"

    def get_success_url(self):
        return reverse_lazy('questionario01.detail', kwargs={'pk': self.object.cirurgia_segura_id})


class Questionario0101DetailView(DetailView):
    model = Questionario0101
    template_name = "questionario/questionario01/questionario0101/questionario0101_detail.html"


class Questionario0101DeleteView(DeleteView):
    model = Questionario0101
    template_name = "questionario/questionario01/questionario0101/questionario0101_delete.html"

    def get_success_url(self):
        return reverse_lazy('questionario01.detail', kwargs={'pk': self.object.cirurgia_segura_id})


########################################## Questionario Cirurgia Pausa ##########################

class Questionario0102PKCreateView(CreateView):
    form_class = Questionario0102Form
    model = Questionario0102
    template_name = "questionario/questionario01/questionario0102//questionario0102_create.html"

    def get_initial(self):
        cirurgia_segura = {'cirurgia_segura': self.kwargs["pk"]}
        return cirurgia_segura

    def get_success_url(self):
        return reverse_lazy('questionario01.detail', kwargs={'pk': self.object.cirurgia_segura_id})


class Questionario0102UpdateView(UpdateView):
    model = Questionario0102
    form_class = Questionario0102Form
    template_name = "questionario/questionario01/questionario0102/questionario0102_update.html"

    def get_success_url(self):
        return reverse_lazy('questionario01.detail', kwargs={'pk': self.object.cirurgia_segura_id})


class Questionario0102DetailView(DetailView):
    model = Questionario0102
    template_name = "questionario/questionario01/questionario0102/questionario0102_detail.html"


class Questionario0102DeleteView(DeleteView):
    model = Questionario0102
    template_name = "questionario/questionario01/questionario0102/questionario0102_delete.html"

    def get_success_url(self):
        return reverse_lazy('questionario01.detail', kwargs={'pk': self.object.cirurgia_segura_id})


########################################## Questionario Cirurgia Saída ####################

class Questionario0103PKCreateView(CreateView):
    form_class = Questionario0103Form
    model = Questionario0103
    template_name = "questionario/questionario01/questionario0103/questionario0103_create.html"

    def get_initial(self):
        cirurgia_segura = {'cirurgia_segura': self.kwargs["pk"]}
        return cirurgia_segura

    def get_success_url(self):
        return reverse_lazy('questionario01.detail', kwargs={'pk': self.object.cirurgia_segura_id})


class Questionario0103UpdateView(UpdateView):
    model = Questionario0103
    form_class = Questionario0103Form
    template_name = "questionario/questionario01/questionario0103/questionario0103_update.html"

    def get_success_url(self):
        return reverse_lazy('questionario01.detail', kwargs={'pk': self.object.cirurgia_segura_id})


class Questionario0103DetailView(DetailView):
    model = Questionario0103
    template_name = "questionario/questionario01/questionario0103/questionario0103_detail.html"


class Questionario0103DeleteView(DeleteView):
    model = Questionario0103
    template_name = "questionario/questionario01/questionario0103/questionario0103_delete.html"

    def get_success_url(self):
        return reverse_lazy('questionario01.detail', kwargs={'pk': self.object.cirurgia_segura_id})


# # class Questionario02ListView(ListView):
# #     model = Questionario02
# #     # context_object_name = 'questionarios02'

# #     # def get_queryset(self):
# #     #     qs = Questionario02.objects.filter(
# #     #         usuario=self.kwargs.get('pk'))
# #     #     return qs

# #     def get_context_data(self, **kwargs):
# #         context = super().get_context_data(**kwargs)
# #         context['questionarios02'] = Questionario02.objects.filter(
# #             usuario=self.kwargs.get('pk'))
# #         context['usuario'] = get_object_or_404(
# #             Usuario, pk=self.kwargs['pk'])
# #         return context


# # class Questionario02DetailView(DetailView):
# #     model = Questionario02
# #     context_object_name = 'questionarios02'

# #     def get_queryset(self):
# #         qs = Questionario02.objects.filter(
# #             usuario=self.kwargs.get('pk'))
# #         return qs


########################################## Questionario 02 ####################











class Questionario02CreateView(CreateView):
    form_class = Questionario02Form
    model = Questionario02
    template_name = "questionario/questionario02/questionario02_create.html"

    # success_url = reverse_lazy('questionario01.detail')

    def get_success_url(self):

        return reverse_lazy('questionario02.detail', kwargs={'pk': self.object.pk})


class Questionario02PKCreateView(CreateView):
    form_class = Questionario02Form
    model = Questionario02
    template_name = "questionario/questionario02/questionario02_create.html"

    def get_success_url(self):
        print(self.object.pk)
        return reverse_lazy('questionario02.detail', kwargs={'pk': self.object.pk})

    def get_initial(self):
        pacientes = Paciente.objects.all()
        print(pacientes)
        return {'paciente': self.kwargs["pk"]}


class Questionario02DetailView(DetailView):
    model = Questionario02
    template_name = "questionario/questionario02/questionario02_detail.html"
    # context_object_name = "questionario01"

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     # context['questionarios0101'] = Questionario0101.objects.all()
    #
    #     context["questionarios0101"] = Questionario0101.objects.filter(
    #         cirurgia_segura_id=self.kwargs.get('pk'))
    #     return context


class Questionario02ListView(ListView):
    model = Questionario02
    template_name = "questionario/questionario02/questionario02_list.html"
    context_object_name = 'questionarios02'

    def get_queryset(self):
        txt_nome = self.request.GET.get('nome_completo')

        if txt_nome:
            usuario = Questionario02.objects.filter(
                paciente__usuario__nome_completo__icontains=txt_nome)

        else:
            usuario = Questionario02.objects.all()

        return usuario


class Questionario02PKListView(ListView):
    model = Questionario02
    template_name = "questionario/questionario02/questionario02pk_list.html"
    context_object_name = 'questionarios02'

    def get_queryset(self):
        qs = Questionario02.objects.filter(paciente=self.kwargs.get('pk'))
        print(qs)
        return qs

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["questionarios01pk"] = Questionario01.objects.filter(
    #         paciente=self.kwargs.get('pk'))
    #     return context


class Questionario02UpdateView(UpdateView):
    model = Questionario02
    form_class = Questionario02Form
    template_name = "questionario/questionario02/questionario02_update.html"

    def get_success_url(self):
        return reverse_lazy('questionario02.detail', kwargs={'pk': self.object.pk})


class Questionario02DeleteView(DeleteView):
    model = Questionario02
    template_name = "questionario/questionario02/questionario02_delete.html"
