from rest_framework import serializers
from .models import Mueble

class MuebleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mueble
        fields = '__all__'