from django.urls import path
from . import views

urlpatterns = [
    path('',views.lista_personas, name='lista_personas'),
    path('persona/<int:pk>/',views.detalle_persona, name='detalle_persona'),
    path('persona/new', views.persona_new, name='persona_new'),
    path('persona/<int:pk>/edit/', views.persona_edit, name='persona_edit'),
    path('animal/',views.lista_animales, name="lista_animales"),
    path('animal/new', views.animal_new, name='animal_new'),
    path('animal/<int:pk>/',views.detalle_animal, name="detalle_animal"),
    path('animal/<int:pk>/edit/', views.animal_edit, name="animal_edit"),
    path('consulta/', views.lista_consultas, name="lista_consultas"),
    path('consulta/new', views.consulta_new, name="consulta_new"),
    path('consulta/<int:pk>/', views.detalle_consulta, name='detalle_consulta'),
    path('consulta/<int:pk>/edit/', views.consulta_edit, name="consulta_edit")
]
