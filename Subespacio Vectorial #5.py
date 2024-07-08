import numpy as np

def verificar_subespacio():
    #Verificar que contiene el vector cero
    vector_cero = np.array([])
    if not np.array_equal(vector_cero, np.array([])):
        return False, "No contiene el vector cero"
    
    #Verificar cerradura bajo la adición
    x1, x2, y1, y2 = 1, 2, 3, 4 #ejemplo de numeros reales
    v1 = np.array([])
    v2 = np.array([])
    suma = v1+v2
    if suma[2] != 4:
        return False, "No es cerrado bajo la adicion"
    
    #Verificar cerradura bajo la multiplicación por escalares
    escalar = 2 #Ejemplo de escalar
    multiplicacion = escalar * v1
    if multiplicacion[2] != 4:
        return False, "No es cerrado bajo la multiplicación por escalares"
    
    return True, "Es un subespacio Vectorial"

es_subespacio, mensaje = verificar_subespacio()
print (mensaje)