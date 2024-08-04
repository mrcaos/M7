from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from rentApp import views
from .views import SignUpView

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',LoginView.as_view(next_page='actualizar_usuario'),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path("signup/", SignUpView.as_view(), name="signup"),
    path('inmuebles', views.InmuebleListView.as_view(), name='inmuebles'),
    path('propiedades',views.propiedades,name='propiedades'),
    path('mispropiedades',views.mispropiedades,name='mispropiedades'),
    path('actualizar_usuario', views.actualizar_usuario, name='actualizar_usuario'),
    path('filtrar-comunas/',views.filtrar_comunas,name='filtrar-comunas'),
    path('inmuebles_buscar/',views.inmuebles_buscar,name='inmuebles_buscar'),
]