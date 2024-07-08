import numpy as np

def es subespacio(vectores):
    if len(vectores) == 0:
        return False, "El conjunto de vectores esta vacío"
    
    dim - len(vectores[0]) #Dimensión del espacio vectorial
    
    #Verificar que contenga el vector cero
    vector_cero = np.zeros(dim)
    if not any ((np.array_equal(vector_cero, v) for v in vectores)):
        return False, "No contiene el vector cero"
    
    #Verificar cerradura bajo la adición
    for v in vectores:
        for w in vectores:
            suma = v + w
            if not any((np.array_equal(suma, u) for u in vectores)):
                return False, "No es cerrado bajo la adición"
            
    #Verificar cerradura bajo la multiplicación por escalares
    for v in vectores:
        for alpha in [-2, 1, 0, 1, 2] #ejemplos de escalares
        multiplicacion = alpha * v
        if not any((np.array_equal(multiplicacion, u) for u in vectores)):
            return False, "No es cerrado bajo la multiplicación por escalares"
        
    return True, "Es un Subespacio Vectorial"

# Ejemplo de uso:
    vectore = [
        np.array([]),
        np.array([]),
        np.array([])
 ]

es_sub, mensaje = es_subespacio(vectores)
print(mensaje)