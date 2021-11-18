from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=50, verbose_name='Titulo')
    subtitle = models.CharField(max_length=200, verbose_name='subtitulo')
    content = models.TextField(verbose_name='contenido')
    image = models.ImageField(verbose_name='Image', upload_to='services')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')


    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'sevicios'
        ordering = ['-created']

    def __str__(self) -> str:
        return self.title

