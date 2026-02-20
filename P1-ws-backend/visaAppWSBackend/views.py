from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.forms.models import model_to_dict
import json
from .pagoDB import verificar_tarjeta, registrar_pago, eliminar_pago, get_pagos_from_db
from .serializers import PagoSerializer

class TarjetaView(APIView):
    def post(self, request):
        datos = request.data
        
        if '_content' in datos:
            try:
                datos = json.loads(datos['_content'])
            except:
                pass
                
        if verificar_tarjeta(datos):
            return Response({'message': 'Datos encontrados en la base de datos'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Datos no encontrados en la base de datos'}, status=status.HTTP_404_NOT_FOUND)

class PagoView(APIView):
    def post(self, request):
        datos = request.data
        
        # PARCHE: Si viene de la web de Django, sacamos el JSON real
        if '_content' in datos:
            try:
                datos = json.loads(datos['_content'])
            except:
                pass

        pago = registrar_pago(datos)
        if pago is None:
            return Response({'message': 'Error al registrar pago.'}, status=status.HTTP_400_BAD_REQUEST)
        
        pago_dict = model_to_dict(pago)
        return Response(pago_dict, status=status.HTTP_200_OK)

    def delete(self, request, id_pago):
        if eliminar_pago(id_pago):
            return Response({'message': 'Pago eliminado con éxito.'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Pago no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

class ComercioView(APIView):
    def get(self, request, idComercio):
        pagos = get_pagos_from_db(idComercio)
        if pagos:
            serializer = PagoSerializer(pagos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'No se encontraron pagos para este comercio.'}, status=status.HTTP_404_NOT_FOUND)