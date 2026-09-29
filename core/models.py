from urllib.parse import quote_plus

from django.db import models


class Denuncia(models.Model):
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Em Andamento', 'Em Andamento'),
        ('Resolvido', 'Resolvido'),
    ]

    CATEGORIA_CHOICES = [
        ('Buraco', 'Buraco'),
        ('Alagamento', 'Alagamento'),
        ('Lixo e Entulho', 'Lixo e Entulho'),
        ('Outro', 'Outro'),
    ]

    categoria = models.CharField(
        max_length=30, choices=CATEGORIA_CHOICES, default='Buraco',
        verbose_name="Tipo de problema"
    )
    rua = models.CharField(max_length=200, verbose_name="Rua / Avenida")
    bairro = models.CharField(max_length=100)
    referencia = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ponto de Referência")
    descricao = models.TextField(verbose_name="Descrição do Problema")
    foto = models.ImageField(upload_to='denuncias/', blank=True, null=True, verbose_name="Foto do Buraco")
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    email_contato = models.EmailField(
        blank=True, null=True,
        verbose_name="E-mail para contato (opcional)",
        help_text="Se preenchido, você recebe um aviso quando o status desta denúncia mudar."
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pendente')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data da Denúncia")

    class Meta:
        ordering = ['-data_criacao']
        verbose_name = "Denúncia"
        verbose_name_plural = "Denúncias"

    @property
    def link_gps(self):
        if self.latitude is not None and self.longitude is not None:
            return f"https://www.google.com/maps/search/?api=1&query={self.latitude},{self.longitude}"
        endereco = f"{self.rua}, {self.bairro}, Paulista, PE"
        return f"https://www.google.com/maps/search/?api=1&query={quote_plus(endereco)}"

    @property
    def tem_coordenadas(self):
        return self.latitude is not None and self.longitude is not None

    def __str__(self):
        return f"{self.rua}, {self.bairro} - {self.status}"
