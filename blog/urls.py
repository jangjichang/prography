from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_index'),
    path('post/list/', PostListView.as_view(), name='post_list'),
    path('post/detail/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),

    path('comment/create/<int:post_pk>/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/update/<int:post_pk>/<int:pk>', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/delete/<int:post_pk>/<int:pk>/', CommentDeleteView.as_view(), name='comment_delete'),
]
