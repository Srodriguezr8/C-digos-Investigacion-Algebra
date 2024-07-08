import numpy as np
## Definimos los vectores
v1 = np.array([1, 1])
v2 = np.array([2, 2])
v3 = np.array([5, 5])

# # Creamos una matriz con los vectores como columnas
matrix = np.column_stack((v1, v2, v3))
#
#Calculamos el rango de la matriz
rank = np.linalg.matrix_rank(matrix)
#
#Verificamos si los vectores forman una base
if rank == 2:
    print("Los vectores forman una base de R^2.")
else:
    print("Los vectores no forman una base de R^2.")