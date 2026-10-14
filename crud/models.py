from django.db import models

# Create your models here.
class Mueble(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre mueble")
    imagen = models.ImageField(upload_to="imagenes/", verbose_name="Imagen", null=True)
    descripcion = models.TextField(verbose_name="Descripcion", null=True)

    def __str__(self):
        fila = 'Nombre:' + self.nombre + ' - ' + 'Descripcion:' + self.descripcion
        return fila

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

