"""
02_funciones_alto_orden.py

Ejemplos del uso de `lambda` junto con funciones de orden superior en Python:
- map
- filter
- sorted
- reduce

Estos ejemplos conectan con la idea del cálculo lambda, donde todo se basa en
funciones que reciben y devuelven funciones.
"""

from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("=== Lista base ===")
print(numeros)
print()


# 1. map + lambda: aplicar una función a cada elemento
# En cálculo lambda sería algo como aplicar (λx. x * x) a cada número.
cuadrados = list(map(lambda x: x * x, numeros))

print("=== map + lambda (cuadrados) ===")
print(cuadrados)
print()


# 2. filter + lambda: quedarnos solo con los números pares
# Idea en cálculo lambda: λx. x es par
pares = list(filter(lambda x: x % 2 == 0, numeros))

print("=== filter + lambda (pares) ===")
print(pares)
print()


# 3. sorted + lambda: ordenar una lista de tuplas por un criterio
personas = [
    ("Ana", 25),
    ("Carlos", 19),
    ("Beatriz", 32),
    ("Daniel", 28),
]

# Ordenar por la edad (posición 1 en la tupla)
personas_ordenadas = sorted(personas, key=lambda p: p[1])

print("=== sorted + lambda (por edad) ===")
print(personas_ordenadas)
print()


# 4. reduce + lambda: acumular un valor (como sumar todo)
# reduce recibe una función acumuladora:
#   λacc. λx. acc + x
suma_total = reduce(lambda acc, x: acc + x, numeros, 0)

print("=== reduce + lambda (suma total) ===")
print("suma_total =", suma_total)
print()


# 5. Lambdas que devuelven funciones (closures)
def multiplicador(factor):
    """
    Devuelve una función que multiplica su argumento por `factor`.
    Similar a: λfactor. (λx. factor * x)
    """
    return lambda x: factor * x  # función generada dinámicamente


por_2 = multiplicador(2)
por_5 = multiplicador(5)

print("=== Lambdas que devuelven funciones (closures) ===")
print("por_2(10) =", por_2(10))  # 20
print("por_5(10) =", por_5(10))  # 50
print()


# 6. Lambdas que reciben funciones
def aplicar(funcion, valor):
    """
    Aplica una función a un valor.
    Ejemplo directo del estilo del cálculo lambda.
    """
    return funcion(valor)


print("=== Lambdas que reciben funciones ===")
print("aplicar(lambda x: x * x, 7) =", aplicar(lambda x: x * x, 7))
print("aplicar(lambda x: x - 1, 10) =", aplicar(lambda x: x - 1, 10))
print()
