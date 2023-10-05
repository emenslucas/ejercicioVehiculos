from modulos.Vehiculo import Vehiculo
from abc import ABC, abstractmethod

class Automovil(Vehiculo):
    ruedas = 4

    def __init__(self, color, marca, aceleracion, anio, modelo):
        super().__init__(anio, modelo)
        self._color = color  
        self._marca = marca  
        self._aceleracion = aceleracion 
        self._velocidad = 0
       
    def acelerar(self):
        self._velocidad += self._aceleracion

    def frenar(self):
        self._velocidad -= self._aceleracion

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def get_marca(self):
        return self._marca

    def set_marca(self, marca):
        self._marca = marca

    def get_aceleracion(self):
        return self._aceleracion

    def set_aceleracion(self, aceleracion):
        self._aceleracion = aceleracion

    def get_velocidad(self):
        return self._velocidad

    def set_velocidad(self, velocidad):
        self._velocidad = velocidad
