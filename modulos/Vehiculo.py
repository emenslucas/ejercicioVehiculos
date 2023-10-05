from abc import ABC, abstractmethod

class Vehiculo(ABC):

  def __init__(self, anio, modelo):
    self.anio = anio
    self.modelo = modelo

  @abstractmethod
  def conducir(self):
    pass

  def get_anio(self):
    return self.anio
  
  def get_modelo(self):
    return self.modelo

  def set_anio(self,anio):
    self.anio = anio

  def set_modelo(self,modelo):
    self.modelo = modelo