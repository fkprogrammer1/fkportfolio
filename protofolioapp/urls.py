
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path("all",views.all,name="all"),
    path("blog/<slug:slug>/",views.singleblog,name='blog')

    
]
