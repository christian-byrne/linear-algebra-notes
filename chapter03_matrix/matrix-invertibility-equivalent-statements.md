
# Matrix Invertibility Equivalent Statements


Gathering together the ways we have to detect if a matrix is invertible (or not).
Let A be a square matrix (n by n). The following statements are equivalent!
- A is invertible
- Determinant of A is nonzero
- rank A=n
- Statements about columns of A:
  - Column vectors of A are Linearly Independent
  - Column vectors of A span n-space
  - Column vectors of A form a basis for n-space
- Av=0 has only the trivial solution (v=[x y z ...] a generic vector).
- Av=b has a unique solution for all constant vectors b in n-space
- Row operations/multiplication by elementary matrices
  - The RREF of A is the n by n identity matrix.
  - A is the product of elementary matrices.
- Rank-Nulity Theorem:
  - Kernel of A is the zero vector.
  - Nullity of A is 0.
  - A is one-to-one.
  - A is onto.
  - Range A is n-space.
- Matrix transpose statements
  - rows of A are linearly independent.
  - rows of A span n-space.
  - rows of A form a basis for n-space.
- Eigenvalues of A are nonzero.
  - 0 is NOT a stretch factor/eigenvalue of A.
  - 0 is NOT an ellipse factor/singular value of A.
