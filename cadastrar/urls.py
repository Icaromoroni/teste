from django.urls import path

from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('cadastrar/', views.index, name='cadastro'),
    path('index/', views.index, name='index'),
    path('sobreviventeViews/<int:id>', views.sobreviventeViews, name='sobrevivente'),
    path('atualizarLocal/<int:id>', views.atualizarViews, name='coordenadas'),
    
]