from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, resolve_url
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.views.generic import *


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    paginate_by = 3

    ordering = ['-created_at']

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(title__icontains=query).order_by('-created_at')
            paginator = Paginator(object_list, 3)
            page = self.request.GET.get('page')

            try:
                posts = paginator.page(page)
            except PageNotAnInteger:
                posts = paginator.page(1)
            except EmptyPage:
                posts = paginator.page(paginator.num_pages)
        else:
            object_list = self.model.objects.order_by('-created_at')
        return object_list

class PostCreateView(CreateView):
    model = Post
    fields = ['author', 'title', 'content']


class PostDetailView(DetailView):
    model = Post


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_index')


class CommentCreateView(CreateView):
    model = Comment
    fields = ['author', 'content']

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = get_object_or_404(Post, pk=self.kwargs['post_pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return resolve_url(self.object.post)


class CommentUpdateView(UpdateView):
    model = Comment
    fields = ['content']

    def get_success_url(self):
        return resolve_url(self.object.post)


class CommentDeleteView(DeleteView):
    model = Comment
    
    def get_success_url(self):
        return resolve_url(self.object.post)