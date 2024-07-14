from django.urls import path
from rentApp import views

urlpatterns = [
    path('inmuebles', views.InmuebleListView.as_view(), name='inmuebles'),
    path('mispropiedades',views.mispropiedades,name='mispropiedades')
]