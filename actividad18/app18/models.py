from django.db import models

class Medico(models.Model):
    id_medico = models.PositiveIntegerField()
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return f"Medico:{self.nombre}, Apellido:{self.apellido}, Especialidad{self.especialidad}"


class Paciente(models.Model):
    id_paciente = models.PositiveBigIntegerField()
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateTimeField
    sexo = models.CharField(max_length=100)
    altura = models.FloatField()
    id_medico = models.ForeignKey(Medico, on_delete=models.CASCADE)


    def __str__(self):
        return f"Paciente:{self.nombre}, Apellido:{self.apellido}, Especialidad{self.fecha_nacimiento}, Sexo{self.sexo}, Altura{self.altura}"

