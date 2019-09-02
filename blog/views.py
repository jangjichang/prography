from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.views.generic import *


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    paginate_by = 7


class PostCreateView(CreateView):
    model = Post
    fields = ['author', 'title', 'content']


class PostDetailView(DetailView):
    model = Post


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:index')


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']