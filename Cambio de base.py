import numpy as np

# Definir la base B
B = np.array([[], []])

# Definir el vector de coordenadas en la base B
x_B = np.array([])

# Convertir a la base estándar
x_estandar = np.dot(B, x_B)

# Imprimir el vector en la base estándar
print("Vector en la base estándar:", x_estandar)
