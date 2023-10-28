from django.views.generic import TemplateView


# Create your views here.


class HomeView(TemplateView):
    template_name = "main/index.html"


class BaseView(TemplateView):
    template_name = "base/base.html"


class Cabecalho(TemplateView):
    template_name = "base/cabeçalho.html"
