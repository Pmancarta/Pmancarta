# seconds = 1042
# minutos = 1042//60
# segundos = 1042 % 60

# print("{} and {}".format(minutos,segundos))

# calcularemos la distancia entre dos planetas.

# first_planet = int(input("Ingresa la distancia al sol del planeta 1 en KM: "))
# second_planet = int(input("Ingresa la distancia al sol del planeta 2 en KM: "))


# distance_km = second_planet - first_planet
# division = first_planet/second_planet
# print(f"La distancia promedio entre la Tierra y Jupiter es de {abs(distance_km)} km.")
# print(round(division, 5))

import numpy as np
import pandas as pd
print(
    "\n\nLes dejo la diferencia entre la tierra y los otros planetas del sistema solar.\n")


# planetas = {"Mercurio": 57909227, "Venus":108209475, "Tierra": 149598262, "Marte":227943824, "Júpiter":778340821, "Saturno":1426666422, "Urano":22870658186, "Neptuno":4498396441, "Pluton":5906376272,}
# tablaPlanetas = pd.DataFrame(data = planetas, columns=["Planetas","Distancia al sol (Km)"])
# print(tablaPlanetas)
# tablaPlanetas = pd.DataFrame({"Planetas":["Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno", "Pluton*"], "Distancias al sol (km)":[57909227, 108209475, 149598262, 227943824,778340821,1426666422,22870658186,4498396441, 5906376272]})
# print(tablaPlanetas)
# # Define los estilos de la tabla
# estilos = [{'selector': 'th', 'props': [('background-color', '#4CAF50'), ('color', 'white'), ('text-align', 'center'), ('border-radius', '15px')]},
#            {'selector': 'td', 'props': [('border', '1px solid grey'), ('text-align', 'center')]},
#            {'selector': 'caption', 'props': [('caption-side', 'top'), ('color', 'blue'), ('font-size', '24px'), ('font-weight', 'bold')]}]

# tabla_estilizada = tablaPlanetas.style.set_table_styles(estilos).hide_index()

# # Muestra la tabla estilizada en la consola

# arr = tablaPlanetas.values
# print(arr)

# for planet in arr:
#     for distan in planet:
#         print(distan)

planets = ["Mercurio", "Venus", "Tierra", "Marte",
           "Júpiter", "Saturno", "Urano", "Neptuno"]
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]

pesoCar = []
for i in gravity_on_planets:
    pesoCar.append(round(i*12650, 2))
print(pesoCar)
print(min(pesoCar))
print(max(pesoCar))
