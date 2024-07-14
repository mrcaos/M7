from django.urls import path
from rentApp import views
from .views import SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('inmuebles', views.InmuebleListView.as_view(), name='inmuebles'),
    path('mispropiedades',views.mispropiedades,name='mispropiedades'),
    path('actualizar_usuario', views.actualizar_usuario, name='actualizar_usuario'),
]