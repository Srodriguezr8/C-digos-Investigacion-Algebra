import numpy as np

# Definir la matriz
matriz = np.array([[], []])

# Calcular el rango de la matriz
rango = np.linalg.matrix_rank(matriz)

# Obtener la imagen de la matriz (columnas linealmente independientes)
_, columnas_independientes = np.linalg.qr(matriz)

# Imprimir el rango y la imagen de la matriz
print("Rango:", rango)
print("Imagen de la matriz:", columnas_independientes)