from django.test import TestCase
from .models import Atrativo, Trilha

class CircuitoTereVerdeTests(TestCase):
    def setUp(self):
        self.atrativo = Atrativo.objects.create(
            nome="Pedra do Sino",
            parque="Parque Nacional da Serra dos Órgãos",
            descricao="Ponto culminante da serra dos órgãos.",
            horario_funcionamento="06:00 às 18:00",
            status_disponibilidade="aberto"
        )
        self.trilha = Trilha.objects.create(
            atrativo=self.atrativo,
            nome="Trilha Principal da Pedra do Sino",
            extensao_km=11.5,
            tempo_estimado_horas=5.0,
            dificuldade="dificil",
            aberta=True
        )

    def test_criacao_atrativo(self):
        self.assertEqual(self.atrativo.nome, "Pedra do Sino")
        self.assertEqual(self.atrativo.status_disponibilidade, "aberto")

    def test_relacao_trilha_atrativo(self):
        self.assertEqual(self.trilha.atrativo.nome, "Pedra do Sino")
        self.assertTrue(self.trilha.aberta)