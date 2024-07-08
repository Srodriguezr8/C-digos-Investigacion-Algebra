import numpy as np
# 
## Definimos los vectores
v1 = np.array([])
v2 = np.array([])
v3 = np.array([])
#
## Crear la matriz con los vectores como columnas
matrix = np.column_stack((v1, v2, v3))
#
# # Calcular el determinante de la matriz
volume = np.abs(np.linalg.det(matrix))
#
print("Formar una base de R3:", volume)