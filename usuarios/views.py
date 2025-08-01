from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, TemplateView, UpdateView
from .form import FormularioRegistroUsuario
from django.urls import reverse_lazy

# Create your views here.
## registro de usuario con clases
class RegistroUsuario(SuccessMessageMixin, CreateView):
    form_class = FormularioRegistroUsuario
    template_name = "usuarios/registro.html"
    success_url = reverse_lazy("login")
    success_message = "usuario registrado correctamente"


class LoginUsuario(LoginView):
    template_name = 'usuarios/login.html'


class LogoutUsuario(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy("home")



"""
Aquí está con funciones

### definir la funcion
## vincular los datos que vienen en tipo post
def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request,"usuarios/registro.html", {"form":form})
"""