from django.urls import path
from App import views

urlpatterns = [
    path('/', views.inicio),
    path('item/', views.item),
    path('objeto/', views.objeto),
    path('usuario/', views.usuario),
]
