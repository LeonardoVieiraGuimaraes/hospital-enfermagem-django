from django.urls import path

from .views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    # path("base", BaseView.as_view(), name="base"),
    # path("cabecalho", Cabecalho.as_view(), name="cabecalho"),
]
