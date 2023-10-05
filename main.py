from modulos.Funciones import sum, res
from modulos.AutomovilVolador import AutomovilVolador

cocheVolador = AutomovilVolador("blanco", "Audi", 150, 2005, "TT", True)

cocheVolador.acelerar()
cocheVolador.acelerar()
cocheVolador.acelerar()

cocheVolador.dejarVolar()

print(f"Velocidad actual del coche volador: {cocheVolador.get_velocidad()} km/h")
print(cocheVolador.isFlying())

print("----------------------------------------------------------------------------")

print(sum(5, 4))

print(res(5, 4))
