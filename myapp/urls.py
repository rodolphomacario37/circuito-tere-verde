from django.urls import path
from .views import (
    AtrativoListCreateView,
    AtrativoDetailView,
    TrilhaListCreateView,
    TrilhaDetailView
)

urlpatterns = [
    path('atrativos/', AtrativoListCreateView.as_view(), name='atrativo-list-create'),
    path('atrativos/<int:pk>/', AtrativoDetailView.as_view(), name='atrativo-detail'),
    path('trilhas/', TrilhaListCreateView.as_view(), name='trilha-list-create'),
    path('trilhas/<int:pk>/', TrilhaDetailView.as_view(), name='trilha-detail'),
]