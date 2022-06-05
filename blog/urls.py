from django.urls import path, include
from . import views
from .views import TweetCreateView

urlpatterns = [

    path('', views.home, name='blog-home'),
    path('post/new/', TweetCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='blog-about'),
    path('post/comment/', views.create_comment, name='post-comment'),

]
