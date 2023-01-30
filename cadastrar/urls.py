from django.urls import path

from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('cadastrar/', views.index, name='cadastro')
]