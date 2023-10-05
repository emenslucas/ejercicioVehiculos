from modulos.Automovil import Automovil

class AutomovilVolador(Automovil):
  ruedas = 6

  def __init__(self, color, marca, aceleracion, anio, modelo, vuela=False):
    super().__init__(color, marca, aceleracion, anio, modelo)
    self.vuela = vuela

  def isFlying(self):
    if self.vuela:
      return "Está volando"
    else:
      return "No está volando"

  def volar(self):
    self.vuela = True

  def dejarVolar(self):
    self.vuela = False

  def vola(self):
    pass

  def conducir(self):
    return "conduciendo"
