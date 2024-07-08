def calcular_base_y_dimension(vectores):
    #verificar que los vectores no sean nulos
    if not vectores:
        raise valueError("El conjunto de vectores no puede estar vacio")
    
    #Definir una función para verificar si un vector es nulo
    def es_vector_nulo(v):
        return all(x == 0 for x in v)
    
    #Eliminar vectores nulos del conjunto
    vectores = [v for v in vectores if not es_vector_nulo(v)]
    
    #Si no quedan vectores después de eliminar los nulos, el subespacio es trivial
    if not vectores:
        return [], 0
    
    #Definir la función para realizar la eliminación de Gauss-Jordan
    def eliminacion_gauss_jordan(matriz):
        if not matriz:
            return matriz
        
        n, n = len(matriz), len(matriz[0])
        for i in range(min(m, n)):
            #Encuentra el indice del elemento máximo en la columna i para evitar divisiones entre cero.
            max_row = max(range(i, m), key-lambda r: abs(matriz[r](i)))
            if matriz[max_row][i] != 0:
                #Intercambiar filas
                matriz[i], matriz[max_row] = matriz[max_row], matriz[i]
                #Normaliza la fila i
                matriz[i] = [x / matriz[i][i]for x in matriz[i]]
                
                #Eliminar otra filas.
                for j in range(m):
                    if i != j:
                        matriz[j] - [matriz[j][k] - matriz[j][i] ´ matriz [i][k] for k in range(n)]
        
        return matriz
    #Convertir los vectores de una matriz
    matriz = [list(v) for v in vectores]
    
    #Aplicar eliminación de Gauss Jordan a la matriz
    matriz_reducida = eliminacion_gauss_jordan(matriz)
    
    #Determinar la independencia lineal mediante el rango de la matriz reducida
    rango = sum(1 for fila in matriz_reducida if any(abs(x) > 1e-10 for x in fila))
    
    #La base del subespacio esta formada por las filas no nulas de la matriz reducida
    base = [fila[:rango] for fila in matriz_reducida if any(abs(x) > 1e-10 for x in fila)]
    
    #La dimensión del subespacio es el rango de la matriz
    dimension = rango
    return base, dimension

#Ejemplos de uso
vectores = [
    [2, -1, ],
    [1, 3, ],
    ]
base, dimension = calcular_base_y_dimension(vectores)

print("Base de subespacio:")
for fila in base:
    print(fila)
print("Dimension del subespacio:", dimension)