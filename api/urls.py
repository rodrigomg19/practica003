from django.urls import path

from . import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('tipo',views.Mantenimiento_TipoView.as_view(),name='tipo'),
    path('tipo/<int:mant_tipo_id>',views.Mantenimiento_Tipo_DetailView.as_view()),
    path('vehiculo',views.Mantenimiento_VehiculoView.as_view(),name='vehiculo'),
    path('vehiculo/<int:mant_vehiculo_id>',views.Mantenimiento_Vehiculo_DetailView.as_view())
]
