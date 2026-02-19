from rest_framework import serializers
from visaApp.models import Tarjeta

class TarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjeta
        fields = '__all__'  