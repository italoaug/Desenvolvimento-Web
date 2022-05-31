from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('adicionar/addmembro/', views.addmembro, name='addmembro'),
    path('apagar/<int:id>', views.apagar, name='apagar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('editar/editarmembro/<int:id>', views.editarmembro, name='editarmembro'),
]

