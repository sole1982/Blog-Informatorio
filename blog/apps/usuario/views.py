from typing import Any
from django.db.models.query import QuerySet
from .forms import RegistroUsuarioForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, DeleteView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Usuario
from django.urls import reverse_lazy 
# Create your views here.

class RegistrarUsuario(CreateView):
    template_name = 'registration/registrar.html'
    form_class = RegistroUsuarioForm

    def form_valid(self, form):
        responde = super().form_valid(form)
        messages.success(self.request, 'Registro exitoso. Por favor, inicia sesión.')
        group = Group.objects.get(name = 'Registrado')
        self.object.groups.add(group)
        form.save()
        return redirect('apps.usuario:registrar')

class LoginUsuario(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        messages.success(self.request, 'Login exitoso.')

        return reverse('apps.usuario:login')
    

class LogoutUsuario(LogoutView):
    template_name = 'registration/logout.html'

    def get_success_url(self):
        messages.success(self.request, 'Logout exitoso.')

        return reverse('apps.usuario:logout')
    
class UsuarioListView(LoginRequiredMixin,DeleteView):
    model= Usuario 
    template_name = 'ususario/usuario_list.html'
    context_object_name = 'usuarios'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.exclude(is_superuser=True)
        return queryset
    
class UsuarioDelteView(LoginRequiredMixin,DeleteView):
    model = Usuario
    template_name = 'usuario/eliminar_usuario.html' 
    success_url = reverse_lazy('apps.usuario:usuario_list')