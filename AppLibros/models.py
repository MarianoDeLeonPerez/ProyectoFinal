from django.db import models

# Create your models here.

class Libros(models.Model):
    nombre=models.CharField(max_length=50)
    autor=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre+" de "+self.autor

class Mangas(models.Model):
    nombre=models.CharField(max_length=50)
    autor=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre+" de "+self.autor

class Comics(models.Model):
    nombre=models.CharField(max_length=50)
    autor=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre+" de "+self.autor