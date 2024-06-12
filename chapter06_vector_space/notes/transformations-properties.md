

> A transformation is determined by how it transforms the elements of a basis.

For transformation $T: V \rightarrow W$:

# Properties of Invertible Transformations

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
  - The transformation of a basis is a basis
  - The transformation of a basis is linearly independent
  - The transformation of a basis spans the codomain
- The columns of the matrix representation are linearly independent

# Properties of Non-Invertible Transformations

- Not invertible
- Either not 1-1 or not onto (making it not square)
  - *Not 1-1*: for every $w \in W$, there is more than one $v \in V$ such that $T(v) = w$
    - The codomain may have more dimensions than the domain
  - *Not onto*: for every $w \in W$, there is no $v \in V$ such that $T(v) = w$
    - The codomain may have fewer dimensions than the domain
- does not map a basis to a basis
  - $det(A) = 0$
- The columns of the matrix representation are linearly dependent