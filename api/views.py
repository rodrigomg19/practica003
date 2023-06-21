from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Mantenimiento_Tipo, Mantenimiento_Vehiculo
from .serializer import Mantenimiento_Tipo_Serializer,Mantenimiento_Vehiculo_Serializer

class IndexView(APIView):
    
    def get(self,request):
        context = {'mensaje':'servidor activo'}
        return Response(context)

#Tabla Tipo Mantenimiento 
# 
class Mantenimiento_TipoView(APIView):
    
    def get(self,request):
        dataTipo = Mantenimiento_Tipo.objects.all()
        serTipo = Mantenimiento_Tipo_Serializer(dataTipo,many=True)
        return Response(serTipo.data)
    
    def post(self,request):
        serTipo = Mantenimiento_Tipo_Serializer(data=request.data)
        serTipo.is_valid(raise_exception=True)
        serTipo.save()
        
        return Response(serTipo.data)
    
class Mantenimiento_Tipo_DetailView(APIView):
    
    def get(self,request,mant_tipo_id):
        dataTipo = Mantenimiento_Tipo.objects.get(pk=mant_tipo_id)
        serTipo = Mantenimiento_Tipo_Serializer(dataTipo)
        return Response(serTipo.data)
    
    def put(self,request,mant_tipo_id):
        dataTipo = Mantenimiento_Tipo.objects.get(pk=mant_tipo_id)
        serTipo = Mantenimiento_Tipo_Serializer(dataTipo,data=request.data)
        serTipo.is_valid(raise_exception=True)
        serTipo.save()
        return Response(serTipo.data)
    
    def delete(self,request,mant_tipo_id):
        dataTipo = Mantenimiento_Tipo.objects.get(pk=mant_tipo_id)
        serTipo = Mantenimiento_Tipo_Serializer(dataTipo)
        dataTipo.delete()
        return Response(serTipo.data)
    
#Tabla Vehiculo Mantenimiento 

class Mantenimiento_VehiculoView(APIView):
    
    def get(self,request):
        dataVehiculo = Mantenimiento_Vehiculo.objects.all()
        serVehiculo = Mantenimiento_Vehiculo_Serializer(dataVehiculo,many=True)
        return Response(serVehiculo.data)
    
    def post(self,request):
        serVehiculo = Mantenimiento_Vehiculo_Serializer(data=request.data)
        serVehiculo.is_valid(raise_exception=True)
        serVehiculo.save()
        
        return Response(serVehiculo.data)
    
class Mantenimiento_Vehiculo_DetailView(APIView):
    
    def get(self,request,mant_vehiculo_id):
        dataVehiculo = Mantenimiento_Vehiculo.objects.get(pk=mant_vehiculo_id)
        serVehiculo = Mantenimiento_Vehiculo_Serializer(dataVehiculo)
        return Response(serVehiculo.data)
    
    def put(self,request,mant_vehiculo_id):
        dataVehiculo = Mantenimiento_Vehiculo.objects.get(pk=mant_vehiculo_id)
        serVehiculo = Mantenimiento_Vehiculo_Serializer(dataVehiculo,data=request.data)
        serVehiculo.is_valid(raise_exception=True)
        serVehiculo.save()
        return Response(serVehiculo.data)
    
    def delete(self,request,mant_vehiculo_id):
        dataVehiculo = Mantenimiento_Vehiculo.objects.get(pk=mant_vehiculo_id)
        serVehiculo = Mantenimiento_Vehiculo_Serializer(dataVehiculo)
        dataVehiculo.delete()
        return Response(serVehiculo.data)
