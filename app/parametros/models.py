from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Etnia(models.Model):
    NombEtni = models.CharField(max_length = 50, verbose_name = "Grupo Etnico") 
    class Meta:
        verbose_name = "Grupo Etnico"
        verbose_name_plural = "Grupos Étnicos"

    #ya creada la clase retornamos el objeto NombEtni, O Nombre de Etnia
    def __str__(self):
        return self.NombEtni

#agregamos las otras clases del modulo:

#clase para el modelo tipoDocu:
class TipoDocu(models.Model):
    NombTiDo = models.CharField(max_length = 50, verbose_name = "Tipo de Documento")
    
    class Meta:
        verbose_name = "Tipo de Documento"
        verbose_name_plural = "Tipo de Documentos"


    def __str__(self):
        return self.NombTiDo

#clasepara el modelo EstaCivil o  Estado Civil:
class EstaCivil(models.Model):
    NomEsci = models.CharField(max_length = 50, verbose_name = "Estado Civil")

    class Meta:
        verbose_name = "Estado Civil"
        verbose_name_plural = "Estados Civiles"


    def __str__(self):
        return self.NomEsci

#Clase para el modelo TipoEstu o clasifficacion de los estudios:

class TipoEstu(models.Model):
    NombTies = models.CharField(max_length = 50, verbose_name = "Tipo de Estudiante")

    class Meta:
        verbose_name = "Tipo de Estudiante"
        verbose_name_plural = "Tipo de Estudiantes"

    def __str__(self):
        return self.NombTies

#clase para el modelo Tipologr o tipo de logro:
class Tipologr(models.Model):
    NombTilo = models.CharField(max_length = 50, verbose_name = "Tipo de Logro")

    class Meta:
        verbose_name = "Tipo de Logro"
        verbose_name_plural = "Tipo de Logros"

    def __str__(self):
        return self.NombTilo
        
