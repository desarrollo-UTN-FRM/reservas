# coding=utf-8

import os

from django.db import models
from django.template.defaultfilters import slugify

from .recurso import Recurso


def establecer_destino_archivo_ubicacion(instance, filename):
    """
    Establece la ruta de destino para el archivo de ubicación cargado a la instancia.
    """
    # Almacena el archivo en:
    # 'app_reservas/ubicaciones/laboratorios_informaticos/<alias>.<extension>'
    ruta_archivos_ubicacion = 'app_reservas/ubicaciones/laboratorios_informaticos/'
    extension_archivo = filename.split('.')[-1] if '.' in filename else ''
    nombre_archivo = '{0!s}.{1!s}'.format(slugify(instance.alias), extension_archivo)
    return os.path.join(ruta_archivos_ubicacion, nombre_archivo)


class LaboratorioInformatico(Recurso):
    # Atributos
    nombre = models.CharField(max_length=50)
    alias = models.CharField(max_length=10)
    capacidad = models.PositiveSmallIntegerField()
    archivo_ubicacion = models.FileField(upload_to=establecer_destino_archivo_ubicacion,
                                         blank=True)
    # Relaciones
    nivel = models.ForeignKey('Nivel')

    class Meta:
        """
        Información de la clase.
        """
        app_label = 'app_reservas'
        ordering = ['alias']
        verbose_name = 'Laboratorio informático'
        verbose_name_plural = 'Laboratorios informáticos'

    def __str__(self):
        """
        Representación de la instancia.
        """
        return 'Laboratorio informático: {0!s}'.format(self.nombre)

    def get_nombre_corto(self):
        """
        Retorna el nombre corto de la instancia.
        """
        return '{0!s} ({1!s})'.format(self.nombre, self.alias)