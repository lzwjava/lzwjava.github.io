---
audio: false
generated: false
image: false
lang: es
layout: post
title: Algebra Lineal
translated: true
---

- La descomposición de valores singulares se puede usar para la compresión de imágenes.
- El determinante de una matriz indica cuánto cambia el área cuando se aplica la matriz a una forma.
- Los valores propios están definidos por la ecuación \[ \det(\lambda I - A) = 0 \].
- El paquete `linalg` de NumPy se puede usar para estudiar y resolver problemas de álgebra lineal.
- Usa transformations de álgebra lineal en espacio n-dimensional para entender matrices.
- Una matriz es un grupo de números arreglados en filas y columnas.
- La ecuación \[ Ax = B \] tiene una solución cuando \[ \text{rank}(A) = \text{rank}([A|B]) \].
- La rank de una matriz es el número de filas (o columnas) linealmente independientes en su forma escalonada.
- ¿Para qué sirve el concepto de rank? Nos dice cuántas filas retienen información durante una transformación lineal. A diferencia de la nullidad (dimensión del espacio nulo), que cuenta cuántas filas se mapean a cero.
- ¿Cuál es la diferencia entre una matriz y un array simple de números? Un array no tiene dirección inherente, mientras que una matriz sí la tiene.
- ¿Cuál es la diferencia entre una matriz y un vector? Un vector es una columna unidimensional de números y tiene una dirección.
- La multiplicación de matrices sigue una regla fija: el número de columnas en la primera matriz debe ser igual al número de filas en la segunda matriz. Una matriz 2×3 multiplicada por una matriz 3×4 da como resultado una matriz 2×4. En la matriz resultante, el valor en la posición (i, j) es el producto punto de la i-ésima fila de la matriz A y la j-ésima columna de la matriz B.
- El determinante de una matriz tiene un significado: si no es igual a 0, la matriz es invertible.