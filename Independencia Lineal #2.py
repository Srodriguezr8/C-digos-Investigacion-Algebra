import numpy as np

# Definir los vectores
v1 = np.array([])
v2 = np.array([])
v3 = np.array([])

# Crear la matriz con estos vectores como filas
matriz = np.array([v1, v2, v3])

# Calcular el rango de la matriz
rango = np.linalg.matrix_rank(matriz)

# Verificar si el rango es menor que el número de vectores
if rango < len(matriz):
    print("El conjunto S es linealmente dependiente.")
else:
    print("El conjunto S es linealmente independiente.")