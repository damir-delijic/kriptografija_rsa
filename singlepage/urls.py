from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("generate_key/<int:num>", views.generate_key, name='generate_key'),
    path("encrypt", views.encrypt, name='encrypt'),
    path("decrypt", views.decrypt, name='decrypt'),
]