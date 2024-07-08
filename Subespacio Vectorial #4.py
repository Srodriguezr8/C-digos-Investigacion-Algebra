import numpy as np
#
## Definamos el conjunto w como una matriz de vectores de la forma (x1, x2, x3, 0)
## Vamos a definir dos vectores en W y un escalar

v1 = np.array([])
v2 = np.array([])
alpha = 2
#
## Verificar si el vector cero esta en W
vector_cero = np.array([])
en_W = np.array_equal(vector_cero, [])
#
## Verificar si W es cerrado bajo la multiplicación escalar
multiplicacion_escalar = alpha * v1
cerrado_multiplicacion = multiplicacion_escalar[3] == 0
#
(en_w, cerrado_suma, cerrado_multiplicacion)