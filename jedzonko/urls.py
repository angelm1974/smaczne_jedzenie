from django.urls import path
from . import views

app_name = 'jedzonko'

urlpatterns = [
    path('producenci/', views.lista_producentow, name='producenci_lista'),
    path('producent/<int:producent_id>/', views.pobierz_producenta,name='producent'),
]   