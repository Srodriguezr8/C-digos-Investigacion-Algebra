import numpy as np

# Definir la función que verifica si una transformación es lineal
def es_transformacion_lineal(L, dimension):
    # Comprobar aditividad
    u = np.random.rand(dimension)
    v = np.random.rand(dimension)
    if not np.allclose(L(u + v), L(u) + L(v)):
        return False
    
    # Comprobar homogeneidad
    c = np.random.rand()
    if not np.allclose(L(c * u), c * L(u)):
        return False
    
    return True

# Definir la transformación L
def L_b(v):
    x, y, z = v
    return np.array([x + 1, y - z])

# Verificar si es transformación lineal
es_lineal = es_transformacion_lineal(L_b, 3)
print(f"L([x, y, z]^T) = [x + 1, y - z]^T es transformación lineal: {es_lineal}")
