from django.db import models

# Create your models here.
class Articulo(models.Model):
    CATEGORIAS = [
        ('COLACION', 'Colación'),
        ('ROPA', 'Ropa'),
    ]

    MODALIDADES = [
        ('REGALO', 'Regalo'),
        ('TRUEQUE', 'Trueque'),
    ]

    ESTADOS = [
        ('DISPONIBLE', 'Disponible'),
        ('RESERVADO', 'Reservado'),
        ('ENTREGADO', 'Entregado'),
    ]

    id = models.AutoField(primary_key=True)
    nombre_articulo = models.CharField(max_length=80, verbose_name='Nombre del artículo')
    categoria = models.CharField(max_length=10, choices=CATEGORIAS, verbose_name='Categoría')
    modalidad = models.CharField(max_length=10, choices=MODALIDADES, verbose_name='Modalidad')
    cantidad = models.PositiveIntegerField(verbose_name='Cantidad')
    a_cambio = models.CharField(max_length=100, blank=True, verbose_name='Qué busco a cambio')
    estado = models.CharField(max_length=12, choices=ESTADOS, verbose_name='Estado')
    nombre_donante = models.CharField(max_length=100, verbose_name='Nombre de contacto')
    fono = models.CharField(max_length=12, verbose_name='Teléfono')
    fecha_publicacion = models.DateField(verbose_name='Fecha de publicación')
    foto = models.ImageField(upload_to='fotos/', verbose_name='Foto')

    def __str__(self):
        return self.nombre_articulo

    def delete(self, using=None, keep_parents=False):
        self.foto.storage.delete(self.foto.name)
        super().delete()