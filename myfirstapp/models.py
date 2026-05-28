from django.db import models

class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    completada = models.BooleanField(default=False)
    creada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Contacto(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"


class Usuario(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    edad = models.IntegerField()
    ciudad = models.CharField(max_length=100)
    # CLAVE: Agregamos el campo para almacenar la contraseña encriptada
    password = models.CharField(max_length=128) 

    def __str__(self):
        return self.username