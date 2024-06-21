

# Linearity Equivalence Class for Transformations

- $A$ is a matrix that represents a linear transformation $T: \mathbb{R}^n \rightarrow \mathbb{R}^m$.
- $T(u + v) = T(u) + T(v)$
- $T(cu) = cT(u)$
- $T(0) = 0$
- $dim(T(\mathbb{R}^n)) = rank(A) + nullity(A)$

# Change of Basis

## Process

> To convert column vector $A$ from an $xy$ coordinate system to an $uv$ coordinate system, multiply the inverse of the matrix found by using the eigenvectors as columns by the column vector $A$.

## Properties

$\forall (A \in \mathbb{R}^{m \times n} | \text{A represents a linear transformation})$:
- If $A$ has $n$ linearly independent eigenvectors, then $A$ is diagonalizable.
  - $(\exists v_1, v_2, \ldots, v_n | \text{v is an eigenvector of A}) \land (v_1, v_2, \ldots, v_n \text{are linearly independent})  \implies \text{A is diagonalizable}$
  - $\forall v (v \in \mathbb{R}^n) \implies \forall v(\text{v is an eigenvector in} \space \mathbb{R}^{n}) \implies \text{A is diagonalizable over} \space \mathbb{R}$

- $A$ is diagonalizable $\implies \exists P \in \mathbb{R}^{n \times n} \space \text{such that} \space P^{-1}AP = D$
  - $D$ is a diagonal matrix
  - $P$ is a matrix with eigenvectors of $A$ as columns

- $A$ is diagonalizable $\implies$ you can rewrite any vector $V$ as a linear combination of the eigenvectors of $A$.
  - $\forall V \in \mathbb{R}^n$ ($V = v_1 \begin{bmatrix} e_1 \\ e_2 \end{bmatrix} + v_2 \begin{bmatrix} e_3 \\ e_4 \end{bmatrix}$)
    - $\begin{bmatrix} e_1 \\ e_2 \end{bmatrix}$ and $\begin{bmatrix} e_3 \\ e_4 \end{bmatrix}$ are the eigenvectors of $A$.
    - $v_1$ and $v_2$ are unknown at this point
  - Simplify by composing the equation into a matrix:
    - (1) Write the eigenvectors of $A$ as columns of a 2x2 matrix $P$
      - $P = \begin{bmatrix} e_1 & e_2 \\ e_3 & e_4 \end{bmatrix}$
    - (2) Rewrite the equation for $V$ as a product of matrices
      - $V = \begin{bmatrix} e_1 & e_2 \\ e_3 & e_4 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \end{bmatrix}$
    - (3) Let $V_1$ and $V_2$ be the initial terms of the vector $V$, then
      - $\begin{bmatrix} V_1 \\ V_2 \end{bmatrix} = \begin{bmatrix} e_1 & e_2 \\ e_3 & e_4 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \end{bmatrix}$
  - Algebraically solve for $v_1$ and $v_2$ by multiplying the inverse of $P$ by $V$
    - $\begin{bmatrix} V_1 \\ V_2 \end{bmatrix} = \begin{bmatrix} e_1 & e_2 \\ e_3 & e_4 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} \implies$
    - $\begin{bmatrix} e_1 & e_2 \\ e_3 & e_4 \end{bmatrix}^{-1} \begin{bmatrix} V_1 \\ V_2 \end{bmatrix} = \begin{bmatrix} e_1 & e_2 \\ e_3 & e_4 \end{bmatrix}^{-1} \begin{bmatrix} e_1 & e_2 \\ e_3 & e_4 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} \implies$
      - *Left-Multiplying both sides by the inverse of the eigenvector matrix*
    - $\begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \begin{bmatrix} e_1 & e_2 \\ e_3 & e_4 \end{bmatrix}^{-1} \begin{bmatrix} V_1 \\ V_2 \end{bmatrix}$
  - Since $V_1$ and $V_2$ are known, and the inverse of the eigenvector matrix is trivial to calculate, $v_1$ and $v_2$ can be found easily this way.
  - This calculation will convert the vector $V$ from the $xy$ coordinate system to the $uv$ coordinate system.
  - Thus, $A$ is diagonalizable $\implies$ you can convert any vector from the $xy$ coordinate system to the $uv$ coordinate system defined by the eigenvectors of $A$.

- $A$ is diagonalizable $\implies$ you can convert any vector back from the $uv$ system to the $xy$ system
  - Since $\begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \begin{bmatrix} e_1 & e_2 \\ e_3 & e_4 \end{bmatrix}^{-1} \begin{bmatrix} V_1 \\ V_2 \end{bmatrix} \implies$
  - $\begin{bmatrix} e_1 & e_2 \\ e_3 & e_4 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \begin{bmatrix} e_1 & e_2 \\ e_3 & e_4 \end{bmatrix} \begin{bmatrix} e_1 & e_2 \\ e_3 & e_4 \end{bmatrix}^{-1} \begin{bmatrix} V_1 \\ V_2 \end{bmatrix} \implies$
  - $\begin{bmatrix} e_1 & e_2 \\ e_3 & e_4 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \begin{bmatrix} V_1 \\ V_2 \end{bmatrix} \implies$
  - $\begin{bmatrix} V_1 \\ V_2 \end{bmatrix} = \begin{bmatrix} e_1 & e_2 \\ e_3 & e_4 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \end{bmatrix}$