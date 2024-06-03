
Since we can view matrices as generalizations of vectors (and, indeed, matrices can and should be thought of as being made up of both row and column vectors), many of the conventions and operations for vectors carry through (in an obvious way) to matrices.


# Equality

Two matrices are equal if they have the same size and their corresponding elements are equal. 

# Addition/Subtraction

Generalizing from vector addition, we can define matrix addition as component-wise addition of each element of the two matrices.

Similarly, matrix subtraction is defined as component-wise subtraction of each element of the two matrices: $A - B = A + (-B)$ where $-B$ is the negative or negation of matrix $B$.

$A + B = \begin{bmatrix} A_{11} + B_{11} & A_{12} + B_{12} & \cdots & A_{1n} + B_{1n} \\ A_{21} + B_{21} & A_{22} + B_{22} & \cdots & A_{2n} + B_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ A_{m1} + B_{m1} & A_{m2} + B_{m2} & \cdots & A_{mn} + B_{mn} \end{bmatrix}$

$A - B = \begin{bmatrix} A_{11} - B_{11} & A_{12} - B_{12} & \cdots & A_{1n} - B_{1n} \\ A_{21} - B_{21} & A_{22} - B_{22} & \cdots & A_{2n} - B_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ A_{m1} - B_{m1} & A_{m2} - B_{m2} & \cdots & A_{mn} - B_{mn} \end{bmatrix}$

# Scalar Multiplication

Scalar multiplication of a matrix is defined as multiplying each element of the matrix by the scalar.

If $A$ is a matrix and $c$ is a scalar, then the **scalar multiple** of $A$ by $c$ is denoted by $cA$.

$c \cdot A = \begin{bmatrix} c \cdot A_{11} & c \cdot A_{12} & \cdots & c \cdot A_{1n} \\ c \cdot A_{21} & c \cdot A_{22} & \cdots & c \cdot A_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ c \cdot A_{m1} & c \cdot A_{m2} & \cdots & c \cdot A_{mn} \end{bmatrix}$

# Matrix Multiplication

The product of two matrices $A$ and $B$ is defined only if the number of columns in $A$ is equal to the number of rows in $B$. If $A$ is an $m \times n$ matrix and $B$ is an $n \times p$ matrix, then the product $AB$ is an $m \times p$ matrix.

If $A$ is an $m \times n$ matrix and $B$ is an $n \times p$ matrix, then the product $AB$ is defined as the $m \times p$ matrix $C$ where each element $C_{ij}$ is the dot product of the $i$th row of $A$ and the $j$th column of $B$.

> $C_{ij} = A_{i1}B_{1j} + A_{i2}B_{2j} + \cdots + A_{in}B_{nj}$


## Reproducing Columns/Rows

Multiplication of a matrix by a standard unit vector can "pick out" or "reproduce" a column or row of the matrix.

consider a 2x3 matrix $A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}$

$\begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix} \cdot A = \begin{bmatrix} 3 \\ 6 \end{bmatrix}$