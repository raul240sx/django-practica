
from django.urls import path
from .views import RegistroUsuario, LoginUsuario, LogoutUsuario

urlpatterns = [
    path("registro/", RegistroUsuario.as_view(), name="registro"),
    path("login/", LoginUsuario.as_view(), name="login"),
    path("logout/", LogoutUsuario.as_view(), name="logout"),
]



""" 
from .views import registro
from django.contrib.auth import views as authview
from django.urls import path

urlpatterns = [
    path("login/", authview.LoginView.as_view(template_name="usuarios/login.html"), name="login"),
    path("logout/", authview.LogoutView.as_view(), name="logout"),
    path("registro/", registro, name="registro")
] 
"""