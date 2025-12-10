"""
03_lambda_y_lambda_calculo.py

Este archivo muestra ejemplos que conectan directamente el cálculo lambda
con funciones `lambda` en Python.

Incluye:
- β-reducción (idea central del cálculo lambda)
- currificación (λx. λy. ...)
- composición de funciones
- funciones como datos (alto orden)
"""

# 1. Ejemplo directo de β-reducción
# Cálculo lambda:
#   (λx. x + 1) 5  →  5 + 1  →  6
f = lambda x: x + 1

print("=== β-reducción informal ===")
print("Definimos f = λx. x + 1 (lambda x: x + 1)")
print("Aplicamos f a 5 → f(5)")
print("Resultado:", f(5))
print()


# 2. Currificación
# Idea en cálculo lambda:
#   λx. λy. x + y
#
# En Python:
suma_curried = lambda x: (lambda y: x + y)

print("=== Currificación ===")
add_10 = suma_curried(10)  # equivalente a fijar x = 10
print("add_10 es una función que suma 10")
print("add_10(5) =", add_10(5))  # → 15
print()


# 3. Composición de funciones
# Idea en cálculo lambda:
#   λf. λg. λx. f (g x)

def componer(f, g):
    """Devuelve una nueva función que representa f ∘ g."""
    return lambda x: f(g(x))


doble = lambda x: x * 2
incrementar = lambda x: x + 3

doble_mas_3 = componer(incrementar, doble)

print("=== Composición de funciones ===")
print("doble_mas_3(4) =", doble_mas_3(4))  # incrementar(doble(4)) = 11
print()


# 4. Funciones como datos (alto orden)
# En cálculo lambda, TODO son funciones.
def aplicar(funcion, valor):
    """Aplica una función a un valor."""
    return funcion(valor)


print("=== Funciones como valores ===")
print("aplicar(lambda x: x * x, 7) =", aplicar(lambda x: x * x, 7))
print("aplicar(lambda x: x - 1, 10) =", aplicar(lambda x: x - 1, 10))
print()


# 5. Ejemplo estilo cálculo lambda paso a paso
"""
Ejemplo teórico:

    (λx. λy. x * y) 3 4
  ≡ ((λx. λy. x * y) 3) 4
  β-reducción paso 1:
      (λy. 3 * y) 4
  β-reducción paso 2:
      3 * 4 = 12
"""

multiplicar_curried = lambda x: (lambda y: x * y)
por_3 = multiplicar_curried(3)
resultado = por_3(4)

print("=== Ejemplo estilo cálculo lambda ===")
print("Multiplicar curried: λx. λy. x * y")
print("por_3 = multiplicador(3) → λy. 3 * y")
print("por_3(4) =", resultado)
print()
