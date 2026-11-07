from rest_framework import serializers
from .models import Atrativo, Trilha

class TrilhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trilha
        fields = '__all__'

class AtrativoSerializer(serializers.ModelSerializer):
    trilhas = TrilhaSerializer(many=True, read_only=True)

    class Meta:
        model = Atrativo
        fields = '__all__'