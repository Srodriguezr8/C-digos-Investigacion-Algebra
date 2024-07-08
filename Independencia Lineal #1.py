import numpy as np

# Definir los vectores
v1 = np.array([])
v2 = np.array([])

# Crear la matriz con estos vectores como filas
matriz = np.array([v1, v2])

# Calcular el determinante
det = np.linalg.det(matriz)

# Verificar si el determinante es cero
if det == 0:
    print("El conjunto S es linealmente dependiente.")
else:
    print("El conjunto S es linealmente independiente.")
