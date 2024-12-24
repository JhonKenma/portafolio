from django.db import models


#creando modelo
class project(models.Model):
    title = models.CharField(max_length=200) 
    description = models.TextField(verbose_name="Descripcion", null=True, blank=True)
    image = models.ImageField(upload_to='projects/images', verbose_name="Imagen", null=True, blank=True)
    url = models.URLField(blank=True)
    
    def __str__(self):
        fila = f"Titulo: {self.title} - Descripción: {self.description}"
        return fila
    
    def delete(self, using=None, keep_parents=False):
        if self.image:
            self.image.storage.delete(self.image.name)
        super().delete(using, keep_parents)
