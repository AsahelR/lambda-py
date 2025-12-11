# lambda-py  
# Cálculo lambda y operador `lambda` en Python  

Este repositorio lo hice con el propósito de entender, de manera sencilla, qué es el **cálculo lambda** y cómo se relaciona con el uso del operador `lambda` en **Python**.  
La idea es aprender lo básico de la teoría y luego ver cómo se aplica en código real.

En pocas palabras:

- El cálculo lambda es un modelo para entender cómo funcionan las funciones.
- En Python usamos `lambda` para crear funciones rápidas y anónimas.
- Aquí trato de unir las dos cosas con ejemplos claros.

---

## 1. ¿Qué es el cálculo lambda?

El **cálculo lambda**, creado por Alonzo Church, es un sistema que permite definir funciones usando lo mínimo posible:  
variables, abstracciones y aplicaciones.  

En este modelo existen solo tres elementos básicos:

- **Variables**: `x`, `y`, `z`…
- **Funciones (abstracción)**: `λx. M`
- **Aplicación**: `(M N)` → aplicar M a N

Ejemplo:

(λx. x + 1) 5 → 6

yaml

Esa “reducción” es lo que se llama **β–reducción**, que básicamente significa reemplazar el parámetro por el valor.

Aunque suene teórico, la idea es exactamente la misma que cuando llamamos una función en cualquier lenguaje.

---

## 2. ¿Qué tiene que ver esto con Python?

Python tiene su propia manera de crear funciones anónimas:

lambda x: x + 1

Y esto se parece mucho a: λx. x + 1.

Se usa cuando queremos:

- funciones rápidas,
- pasar funciones como argumentos (map, filter, sorted),
- evitar escribir un def completo cuando no es necesario.

---

## 3. Estructura del repositorio

lambda-py/  
 ├── README.md  
 └── src/  
     ├── 01_basicos_lambda.py  
     ├── 02_funciones_alto_orden.py  
     └── 03_lambda_y_lambda_calculo.py  

Aquí explico cada archivo.

---

## 4. Explicación de cada archivo

---

### 4.1 `01_basicos_lambda.py` — Uso básico del operador lambda

Incluye ejemplos como:

- diferencia entre def y lambda  
- lambdas con uno y varios parámetros  
- condicionales dentro del lambda  
- uso de map  
- valores por defecto  
- sorted con una función lambda como key  

Ejemplo:

lambda x: "par" if x % 2 == 0 else "impar"

---

### 4.2 `02_funciones_alto_orden.py` — lambda con funciones de orden superior  

Este archivo muestra cómo las funciones pueden recibir o retornar funciones, algo muy relacionado con el cálculo lambda.

---

#### **1. map + lambda**

cuadrados = list(map(lambda x: x * x, numeros))  
nombres_mayus = list(map(lambda s: s.upper(), nombres))

---

#### **2. filter + lambda**

pares = list(filter(lambda x: x % 2 == 0, numeros))  
mayores_que_5 = list(filter(lambda x: x > 5, numeros))

---

#### **3. sorted + lambda**

sorted(personas, key=lambda p: p[1])  
sorted(palabras, key=lambda p: len(p))

---

#### **4. reduce + lambda**

suma_total = reduce(lambda acc, x: acc + x, numeros, 0)  
producto_total = reduce(lambda acc, x: acc * x, numeros, 1)

---

#### **5. Lambdas que devuelven funciones (closures)**

def multiplicador(factor):  
    return lambda x: factor * x

Es parecido a: λfactor.(λx. factor * x)

---

#### **6. Lambdas que reciben funciones**

def aplicar(funcion, valor):  
    return funcion(valor)

Ejemplo:

aplicar(lambda x: x * x, 7)

---

---

### 4.3 `03_lambda_y_lambda_calculo.py` — Conexión directa con el cálculo lambda

Es la parte más teórica, donde se relaciona Python con conceptos del cálculo lambda.

---

#### **1. β–reducción**

f = lambda x: x + 1  
f(5) → 6  

Representa:

(λx. x + 1) 5

---

#### **2. Currificación**

suma_curried = lambda x: (lambda y: x + y)

---

#### **3. Composición de funciones**

def componer(f, g):  
    return lambda x: f(g(x))

---

#### **4. Funciones como datos**

aplicar(lambda x: x * x, 7)

---

#### **5. Ejemplo estilo cálculo lambda**

multiplicar_curried = lambda x: (lambda y: x * y)  
por_3 = multiplicar_curried(3)  
por_3(4) → 12  

Equivale a:

(λx. λy. x * y) 3 4

---

## 5. Conclusión

En este repositorio conecté:

- teoría del cálculo lambda  
- programación funcional en Python  
- ejemplos reales con lambda  

La idea es entender cómo funcionan las funciones anónimas y cómo conceptos teóricos se reflejan en código práctico.
