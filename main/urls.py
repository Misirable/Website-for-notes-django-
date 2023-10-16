from django.urls import path,re_path
from . import views

urlpatterns = [
    re_path(r'^home', views.index, name='home'),         #name='home')
    re_path(r'^create', views.create, name='create') #name='create')
]
