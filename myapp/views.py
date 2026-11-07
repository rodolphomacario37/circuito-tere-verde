from rest_framework import generics, permissions
from .models import Atrativo, Trilha
from .serializers import AtrativoSerializer, TrilhaSerializer

class AtrativoListCreateView(generics.ListCreateAPIView):
    queryset = Atrativo.objects.all()
    serializer_class = AtrativoSerializer
    permission_classes = [permissions.AllowAny]


class AtrativoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Atrativo.objects.all()
    serializer_class = AtrativoSerializer
    permission_classes = [permissions.AllowAny]


class TrilhaListCreateView(generics.ListCreateAPIView):
    queryset = Trilha.objects.all()
    serializer_class = TrilhaSerializer
    permission_classes = [permissions.AllowAny]


class TrilhaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trilha.objects.all()
    serializer_class = TrilhaSerializer
    permission_classes = [permissions.AllowAny]