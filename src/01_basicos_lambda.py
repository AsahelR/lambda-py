"""
01_basicos_lambda.py

Ejemplos básicos del uso de la palabra reservada `lambda` en Python.
La idea es conectar la teoría del cálculo lambda con algo práctico.
"""

# 1. Función tradicional vs función lambda
def cuadrado_def(x):
    """Función normal con def: devuelve el cuadrado de x."""
    return x * x


# La misma idea, pero con una función lambda (función anónima)
# Cálculo lambda: λx. x * x
cuadrado_lambda = lambda x: x * x

print("=== Ejemplo 1: cuadrado ===")
print("cuadrado_def(5)    =", cuadrado_def(5))
print("cuadrado_lambda(5) =", cuadrado_lambda(5))
print()  # línea en blanco


# 2. Lambdas con varios parámetros
# En cálculo lambda podríamos escribir algo como λx. λy. x + y
# En Python lo hacemos directamente con dos parámetros:
sumar = lambda x, y: x + y

print("=== Ejemplo 2: suma ===")
print("sumar(3, 4) =", sumar(3, 4))
print()


# 3. Lambda con expresión condicional (tipo "if" en una sola línea)
# Cálculo lambda (idea): λn. si n es par → "par" si no → "impar"
par_o_impar = lambda n: "par" if n % 2 == 0 else "impar"

print("=== Ejemplo 3: par o impar ===")
for n in range(5):
    print(f"{n} es {par_o_impar(n)}")
print()


# 4. Uso típico: funciones pequeñas "al vuelo" con map
numeros = [1, 2, 3, 4, 5]

# Multiplicar todos los elementos por 10
# En cálculo lambda sería algo como aplicar (λx. x * 10) a cada número.
multiplicados = list(map(lambda x: x * 10, numeros))

print("=== Ejemplo 4: lambda en map ===")
print("números       :", numeros)
print("multiplicados :", multiplicados)
print()


# 5. Lambda con valor por defecto en un parámetro
# Ejemplo: elevar un número a una potencia (por defecto al cuadrado)
potencia = lambda base, exp=2: base ** exp

print("=== Ejemplo 5: parámetros con valor por defecto ===")
print("potencia(3)      =", potencia(3))      # 3^2
print("potencia(2, 3)   =", potencia(2, 3))   # 2^3
print()


# 6. Lambda como clave de ordenamiento (sorted + length)
palabras = ["lambda", "x", "programación", "py"]

# Ordenar por la longitud de cada palabra
ordenadas_por_longitud = sorted(palabras, key=lambda p: len(p))

print("=== Ejemplo 6: lambda como key en sorted ===")
print("original :", palabras)
print("ordenadas:", ordenadas_por_longitud)
print()
