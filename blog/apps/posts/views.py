from typing import Any
from django.shortcuts import redirect
from .models import Post, Comentario, Categoria
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .forms import ComentarioForm, CrearPostForm, NuevaCategoriaForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy 

# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = "post/posts.html"
    context_object_name = "posts"

class PostDetailView(DetailView):
    model = Post
    template_name = "post/post_individual.html"
    context_object_name = "posts"
    pk_url_kwarg = "id"
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ComentarioForm()
        #context['comentarios'] = Comentario.objects.filter(post_id= self.kwargs['id'])
        return context
    
    def posts(self, request, *args, **kwargs):
        form = ComentarioForm(request.Post)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user 
            comentario.posts_id = self.kwargs['id'] 
            comentario.save()
            return redirect('apps.posts:post_individual' , self.kwargs['id'] ) 
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context) 
        
class ComentarioCreateView(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'comentario/agregarComentario.html' 
    success_url= 'comentario/comentarios'

    def form_valid(self, form):
        form.instance.usuario = self.request.userform.instance.posts_id = self.kwargs['id'] 
        return super().form_valid(form)
    
    
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    form_class = CrearPostForm
    template_name = 'post/crear_post.html' 
    success_url= reverse_lazy('apps.posts:posts')
    
class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = NuevaCategoriaForm
    template_name = 'post/crear_categoria.html' 
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        else: 
            return reverse_lazy('apps.posts:post_create')
        
class CategorialistView(ListView):
    model = Categoria
    template_name = 'post/categoria_list.html'
    context_object_name = 'categorias'
    

class CategoriaDeleteView(DeleteView):
    model= Categoria
    template_name = 'post/categoria_confirm_delete.html'
    success_url = reverse_lazy('apps.posts:categoria_list')