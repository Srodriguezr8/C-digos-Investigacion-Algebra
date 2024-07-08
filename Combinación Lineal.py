##Ejercicio 1
import sympy as sp

# Definir los escalares simbólicos
a, b = sp.symbols('a b')

# Definir los vectores de S
v1 = sp.Matrix([])
v2 = sp.Matrix([])

# Definir los vectores a verificar
z = sp.Matrix([])
v = sp.Matrix([])
w = sp.Matrix([])
u = sp.Matrix([])

# Función para verificar si un vector es combinación lineal de v1 y v2
def es_combinacion_lineal(vector):
    combinacion_lineal = a * v1 + b * v2
    ecuaciones = [sp.Eq(combinacion_lineal[0], vector[0]), sp.Eq(combinacion_lineal[1], vector[1]), sp.Eq(combinacion_lineal[2], vector[2])]
    solucion = sp.solve(ecuaciones, (a, b))
    return solucion

# Verificar cada vector
solucion_z = es_combinacion_lineal(z)
solucion_v = es_combinacion_lineal(v)
solucion_w = es_combinacion_lineal(w)
solucion_u = es_combinacion_lineal(u)

print("Solución para z = ():")
print(solucion_z)

print("Solución para v = ():")
print(solucion_v)

print("Solución para w = ():")
print(solucion_w)

print("Solución para u = ():")
print(solucion_u)
