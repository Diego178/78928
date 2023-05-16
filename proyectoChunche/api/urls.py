from django.urls import path
from . import views

urlpatterns = [
    path('temperatura/', views.getTemperatura),
    path('temperatura/agregar', views.postTemperatura),
    path('temperatura/ultimo', views.getTemperaturaUltimo),

    path('calidadAire/', views.getCalidadAire),
    path('calidadAire/agregar', views.postCalidadAire),
    
    # path('put/<int:pk>/', views.putEmployee),
    # path('delete/<int:pk>/', views.deleteEmployee),
    path('hola/', views.getHola),
]