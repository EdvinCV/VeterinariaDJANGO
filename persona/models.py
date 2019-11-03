from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


#Modelo tipo de animal
class TipoAnimal(models.Model):
    nombreTipo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombreTipo

#Modelo de animal
class Animal(models.Model):
    idTipoAnimal = models.OneToOneField(TipoAnimal, on_delete = models.CASCADE)
    nombreAnimal = models.CharField(max_length=50)
    fechaNacimiento = models.DateField('Fecha de Nacimiento')
    raza = models.CharField(max_length=50)
    sexo = models.CharField(max_length=50)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    observaciones = models.TextField()

    def __str__(self):
        return self.nombreAnimal

class Consulta(models.Model):
    sintomas = models.TextField()
    observaciones = models.TextField()
    diagnostico = models.TextField()

class Historial(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    fechaConsulta = models.DateField('Fecha Consulta')
