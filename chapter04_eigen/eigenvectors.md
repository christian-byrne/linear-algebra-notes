
# Process for Finding Eigenvectors and Eigenvalues

## Example Matrix:

$A = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix}$

## Step 1: Find Eigenvalues
To find the eigenvalues, solve the characteristic equation $\text{det}(A - \lambda I) = 0$.

$\text{det} \begin{pmatrix} 4 - \lambda & 1 \\ 2 & 3 - \lambda \end{pmatrix} = (4 - \lambda)(3 - \lambda) - 2 = \lambda^2 - 7\lambda + 10 = 0$

Solve the quadratic equation $\lambda^2 - 7\lambda + 10 = 0$:

$\lambda_1 = 5, \quad \lambda_2 = 2$


## Step 2: Find Eigenvectors
For each eigenvalue, find the corresponding eigenvector by solving $(A - \lambda I)v = 0$.

### Eigenvector for $\lambda_1 = 5$:


$(A - 5I)v = \begin{pmatrix} -1 & 1 \\ 2 & -2 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = 0$

Solve 

$\begin{pmatrix} -1 & 1 \\ 2 & -2 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = 0$:


$-x + y = 0 \implies y = x \quad \Rightarrow \quad v_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$

#### Eigenvector for $\lambda_2 = 2$:


$(A - 2I)v = \begin{pmatrix} 2 & 1 \\ 2 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = 0$

Solve

$\begin{pmatrix} 2 & 1 \\ 2 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = 0$:

$2x + y = 0 \implies y = -2x \quad \Rightarrow \quad v_2 = \begin{pmatrix} 1 \\ -2 \end{pmatrix}$

## Step 3: Form $D$ and $P$

Form the diagonal matrix $D$ with the eigenvalues and the matrix $P$ with the eigenvectors as columns.

$D = \begin{pmatrix} 5 & 0 \\ 0 & 2 \end{pmatrix}, \quad P = \begin{pmatrix} 1 & 1 \\ 1 & -2 \end{pmatrix}$

## Step 4: Verify $P^{-1}AP = D$

Compute $P^{-1}$ and verify the equation $P^{-1}AP = D$.

1. Find $P^{-1}$:

$P^{-1} = \frac{1}{\text{det}(P)} \begin{pmatrix} -2 & -1 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} \frac{2}{3} & \frac{1}{3} \\ \frac{1}{3} & -\frac{1}{3} \end{pmatrix}$


2. Compute $P^{-1}AP$:

$P^{-1}AP = \begin{pmatrix} \frac{2}{3} & \frac{1}{3} \\ \frac{1}{3} & -\frac{1}{3} \end{pmatrix} \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 1 & -2 \end{pmatrix}$


Thus, we have verified that $P^{-1}AP = D$.

## Change of Basis

### To Eigenbasis

Whole matrix: $A = PDP^{-1}$

Vector: $x_{\text{eigenbasis}} = P^{-1}x$

### To Standard Basis

Whole matrix: $A = PDP^{-1}$

Vector: $x_{\text{standard}} = Px$

## Summary

1. Find eigenvalues by solving $\text{det}(A - \lambda I) = 0$.
2. Find eigenvectors by solving $(A - \lambda I)v = 0$ for each eigenvalue.
3. Form $D$ from eigenvalues and $P$ from eigenvectors.
4. Verify $P^{-1}AP = D$.

# Important Notes

- **Linear Dependence**: The eigenvectors must be linearly independent to form a valid basis (and thus $P$ must be invertible).
- **Invertibility of P**: If $P$ is not invertible, the matrix $A$ is not diagonalizable. I.e., its determinant should be non-zero in order to change the bases back and forth
- **Complex Eigenvalues**: If the matrix has complex eigenvalues, the eigenvectors will be complex as well. The real and imaginary parts of the eigenvectors form a basis for the eigenspace.
- **Repeated Eigenvalues**: If an eigenvalue has a multiplicity greater than one, there may be fewer than $n$ linearly independent eigenvectors. In this case, the matrix is still diagonalizable if the eigenvectors are linearly independent.
- **Generalization**: The process can be generalized to $n \times n$ matrices.

# Note about the Ordering of the Eigenvalues in the Diagonal Matrix

The eigenvalues in the diagonal matrix $D$ are ordered according to the columns of the matrix $P$. The first column of $P$ corresponds to the first eigenvalue in $D$, the second column of $P$ corresponds to the second eigenvalue in $D$, and so on.

![alt text](pictures/eigenvalue-ordering.png)
