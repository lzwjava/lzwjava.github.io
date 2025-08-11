---
audio: false
generated: false
image: false
lang: en
layout: post
title: Linear Algebra
translated: false
---

- Singular Value Decomposition can be used for image compression.

- The determinant of a matrix indicates how much the area changes when the matrix is applied to a shape.

- The eigenvalues are defined by the equation \\[ \det(\lambda I - A) = 0 \\].

- NumPy's `linalg` package can be used to study and solve problems in linear algebra.

- Use linear-algebra transforms in n-dimensional **space** to understand matrices.

- A matrix is a group of numbers arranged in rows and columns.

- The equation \\[ Ax = B \\] has a solution when \\[ \text{rank}(A) = \text{rank}([A|B]) \\].

- The rank of a matrix is the number of linearly independent rows (or columns) in its **echelon form**.

---

What is the use of the rank concept? It tells us how many rows retain information during a linear transformation. In contrast, the nullity (dimension of the null space) counts how many rows are mapped to zero.

What is the difference between a matrix and a plain array of numbers? An array has no inherent direction, whereas a matrix does.  

What is the difference between a matrix and a vector? A vector is a one-dimensional column of numbers and has a direction.

The matrix multiplation has some fixed rule -- the column of first matrix should be eqaul to the row of second matrix. The 2x3 matrix mupltiply the 3x4 matrix euqals another matrix - the size is 2 x 4.  For the result matrix, the value at position (i, j) means that the i row of the matrix A muplitply the j column of the matrix B. They do some thorough communication.

The determinant of matrix has some meaning. If it isn't equal to 0 , that means the matrix is reversiable.

