import sympy as sp

def suma_vectorial(v1, v2):
    return (v1[] + v2[], v1[] + v2[], v1[] + v2[], v1[] + v2[])

def multiplicacion_escalar(c, v):
    return (c * v[], c * v[], c * v[], c * v[])

def es_subespacio_vectorial():
    # Definir variables simbólicas
    x1, y1, z1, w1 = sp.symbols('x1 y1 z1 w1')
    x2, y2, z2, w2 = sp.symbols('x2 y2 z2 w2')
    c = sp.symbols('c')

    # Vectores en W
    v1 = (x1, y1, z1, 0)
    v2 = (x2, y2, z2, 0)
    v0 = (0, 0, 0, 0)

    # 1. Cerradura bajo la suma
    suma_v1_v2 = suma_vectorial(v1, v2)
    if suma_v1_v2[3] != 0:
        print("Falló la cerradura bajo la suma")
        return False

    # 2. Cerradura bajo la multiplicación por un escalar
    escalar_v1 = multiplicacion_escalar(c, v1)
    if escalar_v1[3] != 0:
        print("Falló la cerradura bajo la multiplicación por un escalar")
        return False

    # 3. Contiene el vector cero
    if v0 not in [v1, v2]:
        print("No contiene el vector cero")
        return False

    return True

# Ejecutar la verificación
print(es_subespacio_vectorial())  # Debería imprimir True o False
