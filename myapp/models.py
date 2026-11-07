from django.db import models

class Atrativo(models.Model):
    STATUS_CHOICES = [
        ('aberto', 'Aberto'),
        ('fechado', 'Fechado'),
        ('temporada', 'Temporada Especial'),
    ]

    nome = models.CharField(max_length=120)
    parque = models.CharField(max_length=120)  # Ex: PARNASO, Três Picos
    descricao = models.TextField()
    horario_funcionamento = models.CharField(max_length=100)
    status_disponibilidade = models.CharField(max_length=20, choices=STATUS_CHOICES, default='aberto')

    def __str__(self):
        return f"{self.nome} - {self.parque}"


class Trilha(models.Model):
    NIVEL_DIFICULDADE = [
        ('facil', 'Fácil'),
        ('moderada', 'Moderada'),
        ('dificil', 'Difícil'),
    ]

    atrativo = models.ForeignKey(Atrativo, related_name='trilhas', on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    extensao_km = models.DecimalField(max_digits=5, decimal_places=2)
    tempo_estimado_horas = models.DecimalField(max_digits=4, decimal_places=1)
    dificuldade = models.CharField(max_length=20, choices=NIVEL_DIFICULDADE, default='facil')
    aberta = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} ({self.dificuldade})"