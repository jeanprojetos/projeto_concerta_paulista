from django.db import models

class Denuncia(models.Model):
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Em Andamento', 'Em Andamento'),
        ('Resolvido', 'Resolvido'),
    ]

    rua = models.CharField(max_length=200, verbose_name="Rua / Avenida")
    bairro = models.CharField(max_length=100)
    referencia = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ponto de Referência")
    descricao = models.TextField(verbose_name="Descrição do Problema")
    foto = models.ImageField(upload_to='denuncias/', blank=True, null=True, verbose_name="Foto do Buraco")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pendente')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data da Denúncia")

    @property
    def link_gps(self):
        endereco = f"{self.rua}, {self.bairro}, Paulista, PE"
        endereco_formatado = endereco.replace(" ", "+")
        return f"https://www.google.com/maps/search/?api=1&query={endereco_formatado}"

    def __str__(self):
        return f"{self.rua}, {self.bairro} - {self.status}"