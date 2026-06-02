from django.db import models

class Documento(models.Model):
    nome = models.CharField(max_length=255)
    pdf = models.FileField(upload_to='pdfs/')
    texto = models.TextField(blank=True)

    def __str__(self):
        return self.nome