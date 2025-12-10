# lambda-py
# Cálculo lambda y operador `lambda` en Python 

Este repositorio es una mini guía para entender qué es el **cálculo lambda** y cómo se relaciona con el uso del operador `lambda` en **Python**.

La idea es muy sencilla:

- En la teoría, el cálculo lambda nos sirve para entender qué es “computar” usando solo funciones.
- En la práctica, en Python usamos `lambda` para crear funciones “rápidas” y anónimas.
- Aquí conectamos las dos cosas: un poco de teoría y varios ejemplos en código.

---

## 1. ¿Qué es el cálculo lambda? (versión sin dolor)

El **cálculo lambda** es un modelo matemático de computación que inventó Alonzo Church.  
Suena muy rimbombante, pero la base es esta:

Solo trabajamos con:

- **Variables**: `x`, `y`, `z`, …
- **Funciones** (abstracción): algo como `λx. M`
- **Aplicación**: aplicar una función a un valor, algo como `(M N)`

La forma típica de una función en cálculo lambda es:

```text
λx. M


