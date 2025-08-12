from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_comments, name='list_comments'),
    path('post/', views.post_comment, name='post_comment'),
    path('<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
