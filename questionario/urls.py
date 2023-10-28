from django.urls import path

from .views import Questionario0101PKCreateView, Questionario0101UpdateView, Questionario01CreateView, \
    Questionario01DetailView, Questionario01ListView, Questionario01PKCreateView, Questionario01PKListView, \
    Questionario01UpdateView, Questionario0101DetailView, Questionario0101DeleteView, Questionario0102PKCreateView, \
    Questionario0102UpdateView, Questionario0102DetailView, Questionario0102DeleteView, Questionario0103PKCreateView, \
    Questionario0103UpdateView, Questionario0103DetailView, Questionario0103DeleteView, Questionario02CreateView, \
    Questionario02PKCreateView, Questionario02DetailView, Questionario02PKListView, Questionario02UpdateView, \
    Questionario02ListView

urlpatterns = [
    # path("", QuestionarioView.as_view(), name="questionario.home"),

    ##################################### Questionario01 Cirurgia #########################

    path("cadastrar01/", Questionario01CreateView.as_view(),
         name="questionario01.create"),
    path("cadastrar01pk/<int:pk>", Questionario01PKCreateView.as_view(),
         name="questionario01pk.create"),
    path("detalhar01/<int:pk>", Questionario01DetailView.as_view(),
         name="questionario01.detail"),
    path("listar01", Questionario01ListView.as_view(),
         name="questionario01.list"),
    path("listar01pk/<int:pk>", Questionario01PKListView.as_view(),
         name="questionario01pk.list"),
    path("atualizar01/<int:pk>", Questionario01UpdateView.as_view(),
         name="questionario01.update"),

    ##################################### Questionario0101 Cirurgia #########################

    path("cadastrar0101/<int:pk>", Questionario0101PKCreateView.as_view(),
         name="questionario0101pk.create"),
    path("atualizar0101/<int:pk>", Questionario0101UpdateView.as_view(),
         name="questionario0101.update"),
    path("detalhar0101/<int:pk>", Questionario0101DetailView.as_view(),
         name="questionario0101.detail"),
    path("ddeletar0101/<int:pk>", Questionario0101DeleteView.as_view(),
         name="questionario0101.delete"),

    ##################################### Questionario0102 Cirurgia #########################

    path("cadastrar0102/<int:pk>", Questionario0102PKCreateView.as_view(),
         name="questionario0102pk.create"),
    path("atualizar0102/<int:pk>", Questionario0102UpdateView.as_view(),
         name="questionario0102.update"),
    path("detalhar0102/<int:pk>", Questionario0102DetailView.as_view(),
         name="questionario0102.detail"),
    path("ddeletar0102/<int:pk>", Questionario0102DeleteView.as_view(),
         name="questionario0102.delete"),

    ################################### Questionario0103 Cirurgia #########################

    path("cadastrar0103/<int:pk>", Questionario0103PKCreateView.as_view(),
         name="questionario0103pk.create"),
    path("atualizar0103/<int:pk>", Questionario0103UpdateView.as_view(),
         name="questionario0103.update"),
    path("detalhar0103/<int:pk>", Questionario0103DetailView.as_view(),
         name="questionario0103.detail"),
    path("ddeletar0103/<int:pk>", Questionario0103DeleteView.as_view(),
         name="questionario0103.delete"),

    ################################### Questionario02 Cirurgia #########################

    path("cadastrar02/", Questionario02CreateView.as_view(),
         name="questionario02.create"),
    path("cadastrar02pk/<int:pk>", Questionario02PKCreateView.as_view(),
         name="questionario02pk.create"),
    path("detalhar02/<int:pk>", Questionario02DetailView.as_view(),
         name="questionario02.detail"),
    path("listar02", Questionario02ListView.as_view(),
         name="questionario02.list"),
    path("listar02pk/<int:pk>", Questionario02PKListView.as_view(),
         name="questionario02pk.list"),
    path("atualizar02/<int:pk>", Questionario02UpdateView.as_view(),
         name="questionario02.update"),

    #     path("cadastrar01pk/<int:pk>", Questionario0101PKCreateView.as_view(),
    #          name="questionario01pk.create"),

    #     path("listar01", Questionario0101ListView.as_view(),
    #          name="questionario01.list"),
    #     path("listar01pk/<int:pk>", Questionario0101PKListView.as_view(),
    #          name="questionario01pk.list"),
    #     path("atualizar01/<int:pk>", Questionario0101UpdateView.as_view(),
    #          name="questionario01.update"),

    #     path("listar0101/<int:pk>", Questionario0101ListView.as_view(),
    #          name="questionario0101.listar"),

    # path("cadastrar0102/<int:pk>", Questionario0102CreateView.as_view(),
    #      name="questionario0102.cadastrar"),

    # path("cadastrar0103/<int:pk>", Questionario0103CreateView.as_view(),
    #      name="questionario0103.cadastrar"),

    # path("cadastrar0104/<int:pk>", Questionario0104CreateView.as_view(),
    #      name="questionario0104.cadastrar"),

    # path("cadastrar02/<int:pk>", Questionario02CreateView.as_view(),
    #      name="questionario02.cadastrar"),

    # path("listar01/<int:pk>", Questionario0101ListView.as_view(),
    #      name="questionario01.listar"),

    # path("listar02/<int:pk>", Questionario02ListView.as_view(),
    #      name="questionario02.listar"),

    # path("detalhar02/<int:pk>", Questionario02DetailView.as_view(),
    #      name="questionario02.detalhar"),
]
