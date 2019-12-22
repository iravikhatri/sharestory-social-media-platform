from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('post/liked', views.liked_posts, name="liked_posts"),
    path('post/create/', views.post_create, name="post_create"),
    path('post/like/', views.post_like, name="post_like"),
]
