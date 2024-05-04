from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='blog'),    
    path('prouduct', views.prouduct, name='blog'),
    path('apout', views.apout, name='blog'),
    # path('<int:post_id>/', views.Post, name='blog_detail'),
    ]