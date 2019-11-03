from django.urls import path
from . import views

urlpatterns = [
    path('',views.lista_personas, name='lista_personas'),
    path('persona/<int:pk>/',views.detalle_persona, name='detalle_persona'),
    path('persona/new', views.nueva_persona, name='persona_new'),
]
