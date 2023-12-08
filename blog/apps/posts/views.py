from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
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

