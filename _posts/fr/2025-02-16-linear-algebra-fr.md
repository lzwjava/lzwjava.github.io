---
audio: false
generated: false
image: false
lang: fr
layout: post
title: Algebra Linéaire
translated: true
---

- La décomposition en valeurs singulières peut être utilisée pour la compression d'images.
- Le déterminant d'une matrice indique combien la surface change lorsqu'elle est appliquée à une forme.
- Les valeurs propres sont définies par l'équation ![\\det(\\lambda I - A) = 0]().
- Le package `linalg` de NumPy peut être utilisé pour étudier et résoudre des problèmes en algèbre linéaire.
- Utilisez des transformations d'algèbre linéaire dans l'espace à n dimensions pour comprendre les matrices.
- Une matrice est un groupe de nombres disposés en rangées et colonnes.
- L'équation ![Ax = B]() a une solution lorsque ![ran(A) = ran([A|B])]().
- Le rang d'une matrice est le nombre de lignes (ou colonnes) linéairement indépendantes dans sa forme échelonnée.
---

Qu'est-ce que le concept de rang ? Il nous dit combien de lignes conservent des informations pendant une transformation linéaire. À l'inverse, la nullité (dimension de l'espace nul) compte combien de lignes sont mappées à zéro.

 Quelle est la différence entre une matrice et un tableau plain de nombres ? Un tableau n'a pas de direction inhérente, contrairement à une matrice.
Quelle est la différence entre une matrice et un vecteur ? Un vecteur est une colonne unidimensionnelle de nombres et a une direction.

La multiplication matricielle suit une règle fixe : le nombre de colonnes dans la première matrice doit égaler le nombre de rangées dans la deuxième matrice. La multiplication d'une matrice 2×3 par une matrice 3×4 donne une matrice 2×4. Dans la matrice résultante, la valeur à la position (i, j) est le produit scalaire de la ième rangée de la matrice A et de la jème colonne de la matrice B.

Le déterminant d'une matrice a une signification : s'il n'est pas égal à 0, la matrice est inversible.