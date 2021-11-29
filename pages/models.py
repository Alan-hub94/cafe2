from django.db import models

class Policy(models.Model):
    title = models.CharField(verbose_name='Titulo', max_length=50)
    content = models.TextField(verbose_name='Contenido')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualizacion')

    class Meta:
        verbose_name = 'Politica'
        verbose_name_plural = 'Politicas'

    def __str__(self) -> str:
        return self.title