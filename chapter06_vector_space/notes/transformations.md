

> A transformation is determined by how it transforms the elements of a basis.

For transformation $T: V \rightarrow W$:

# Invertibility

## Properties of Invertible Transformations

- Invertible
  - there is another transformation $T^{-1}: W \rightarrow V$ such that $T^{-1} \circ T = I_V$ and $T \circ T^{-1} = I_W$
  - there is another transformation $T^{-1}: W \rightarrow V$ such that $T^{-1}(T(u)) = u$ for all $u \in V$
- 1-1 (injective) and Onto (surjective)
  - *1-1*: for every $w \in W$, there is at most one $v \in V$ such that $T(v) = w$
  - *Onto*: for every $w \in W$, there is at least one $v \in V$ such that $T(v) = w$
- Square
  - $T$ maps n-dimensional space to n-dimensional space
  - If it is not square because the codomain is smaller, then it is not onto
  - If it is not square because the domain is smaller, then it is not 1-1
  - The matrix representation of a square transformation is a square matrix
- Maps a basis to a basis
  - $det(A) \neq 0$
  - The columns of the matrix representation are linearly independent
  - The transformation of a basis spans the codomain

## Properties of Non-Invertible Transformations

- Not invertible
- Either not 1-1 or not onto (making it not square)
  - *Not 1-1*: for every $w \in W$, there is more than one $v \in V$ such that $T(v) = w$
    - The codomain may have more dimensions than the domain
  - *Not onto*: for every $w \in W$, there is no $v \in V$ such that $T(v) = w$
    - The codomain may have fewer dimensions than the domain
- does not map a basis to a basis
  - The columns of the matrix representation are linearly dependent
  - $det(A) = 0$

# Identity Matrix

The identity matrix is a square matrix with 1s on the diagonal and 0s elsewhere. It is denoted by $I_n$ or simply $I$ if the size is clear from the context.

The identity matrix maps each standard basis vector to itself.

# Inverse Matrix

The inverse of a square matrix $A$ is denoted by $A^{-1}$ and is defined such that $A^{-1}A = I$ and $AA^{-1} = I$.

## Relationship with Row Operations

Multiplying ont he left by an elementary matrix $E$ is equivalent to applying the row operation represented by $E$ to the identity matrix.

For example, a vertical shear matrix $S$ can be constructed by multiplying the identity matrix by an elementary matrix $E$ that represents a vertical shear operation.

$E = \begin{bmatrix} 1 & 0 \\ 2 & 1 \end{bmatrix}$

$S = E \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 2 & 1 \end{bmatrix}$

## Algorithm for Finding the Inverse of a Matrix

1. Augment the matrix with its identity matrix
2. Perform row operations to transform the left side into the identity matrix
3. The right side is the inverse of the original matrix



# Determinant

The determinant of a square matrix $A$ is denoted by $det(A)$ and is a scalar value that represents how the matrix scales the volume of a unit cube.

The determinant of a matrix is non-zero if and only if the matrix is invertible.

# Rank

The rank of a matrix is the maximum number of linearly independent rows or columns in the matrix. It is denoted by $rank(A)$.

# Nullity

The nullity of a matrix is the number of free variables in the solution to the homogeneous system $Ax = 0$. It is denoted by $nullity(A)$.

# Compositions

- The composition of invertible transformations is invertible
- The codomain of the first transformation must match the domain of the second transformation (in terms of dimensions)
  - Remember by pairing the closest dimensions when put side by side