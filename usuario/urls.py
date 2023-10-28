from django.urls import path

from .views import PacienteCreateView, PacienteDeleteView, PacienteDetailView, PacienteListView, PacientePKCreateView, \
    PacienteUpdateView, UsuarioCreateView, UsuarioDetailView, UsuarioListView, UsuarioUpdateView, UsuarioDeleteView, \
    PacientePKListView

urlpatterns = [

    ################################ Url para Usuario ############################
    # path("", UsuarioView.as_view(), name="usuario.home"),

    path("usuario_cadastrar", UsuarioCreateView.as_view(),
         name="usuario.create"),

    path("usuario_listar", UsuarioListView.as_view(),
         name="usuario.list"),

    path("usuario_atualizar/<int:pk>",
         UsuarioUpdateView.as_view(), name="usuario.update"),

    path("usuario_detalhar/<int:pk>",
         UsuarioDetailView.as_view(), name="usuario.detail"),

    path("usuario_detetar/<int:pk>",
         UsuarioDeleteView.as_view(), name="usuario.delete"),

    ################################ Url para Usuario #####################################

    path("paciente_cadastrar", PacienteCreateView.as_view(),
         name="paciente.create"),

    path("paciente_cadastrar/<int:pk>", PacientePKCreateView.as_view(),
         name="pacientepk.create"),

    path("paciente_listar/", PacienteListView.as_view(),
         name="paciente.list"),

    path("pacientepk_listar/<int:pk>", PacientePKListView.as_view(),
         name="pacientepk.list"),

    path("paciente_atualizar/<int:pk>",
         PacienteUpdateView.as_view(), name="paciente.update"),

    path("paciente_detalhar/<int:pk>",
         PacienteDetailView.as_view(), name="paciente.detail"),

    path("paciente_detetar/<int:pk>",
         PacienteDeleteView.as_view(), name="paciente.delete"),

    #################################################################
    # path("", UsuarioView.as_view(), name="usuario.home"),

    #     path("usuario_cadastrar", UsuarioCreateView.as_view(),
    #          name="usuario.create"),

    #     path("usuario_listar", UsuarioListView.as_view(), name="usuario.list"),

    #     path("usuario_editar/<int:pk>",
    #          UsuarioUpdateView.as_view(), name="usuario.update"),

    #     path("usuario_detalhar/<int:pk>",
    #          UsuarioDetailView.as_view(), name="usuario.detail"),

    #     ############################### Url para Paciente#####################################

    #     #     path("paciente_cadastrar", PacienteCreateView.as_view(),
    #     #          name="paciente.cadastrar"),

    #     #     path("paciente_listar", PacienteListView.as_view(), name="paciente.listar"),

    #     #     path("paciente_editar/<int:pk>",
    #     #          PacienteUpdateView.as_view(), name="paciente.editar"),

    #     #     path("paciente_detalhar/<int:pk>", PacienteDetailView.as_view(),
    #     #          name="paciente.detalhar"),

    #     # path("detalhar/<int:pk>", UsuarioDetailView.as_view(), name="usuario.detalhar"),

    #     # path("deletar/<int:pk>", UsuarioDeleteView.as_view(), name="usuario.deletar"),
]
