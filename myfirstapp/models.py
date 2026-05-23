from django.db import models

class Contacto(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    # Corregido: Ahora tiene doble guion bajo __str__
    def __str__(self):
        return f"{self.name} - {self.email}"

class Usuario(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    edad = models.IntegerField()
    ciudad = models.CharField(max_length=100)
    
    # Opcional: También le puedes agregar un __str__ a Usuario para verlos 
    # ordenados por su username en el admin de Django.
    def __str__(self):
        return self.username