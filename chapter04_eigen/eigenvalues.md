
# Complex Eigenvalues


## Conversion to Polar Form

$a + bi$

$r = \sqrt{a^2 + b^2}$

$\theta = \arctan{\frac{b}{a}}$

## Conversion to Real Eigenvalues

1. $\sin{\pi} = 0$ $\implies$
2. $i * \sin{\pi} = 0$ $\implies$
3. $\cos{\pi} + i\sin{\pi} = -1$
4. Since $e^{ix} = \cos{x} + i\sin{x}$, then
5. $e^{\pi * i} = -1$
6. Therefore, to convert complex eigenvalues (that are in polar form) to real eigenvalues, continuously find the compose of the transformation until the exponent is of the form $k * pi * i$.
7. The number of iterations of the transformation required indicates the power of $V$ required for the respective eigenvalues to be real stretch factors for the transformation.


## Example

$A = \begin{bmatrix} 2 & -1 \\ 1 & 2 \end{bmatrix}$

$\lambda = 2 + i$

$r = \sqrt{2^2 + 1^2} = \sqrt{5}$

$\theta = \arctan{\frac{1}{2}}$

$\theta = 0.4636$

$\lambda = 2 + i = \sqrt{5}e^{0.4636i}$

$A = PDP^{-1}$

$P = \begin{bmatrix} 1 & 1 \\ -i & i \end{bmatrix}$

$D = \begin{bmatrix} 2 + i & 0 \\ 0 & 2 - i \end{bmatrix}$

$P^{-1} = \begin{bmatrix} 0.5 & 0.5i \\ 0.5 & -0.5i \end{bmatrix}$

$A = \begin{bmatrix} 1 & 1 \\ -i & i \end{bmatrix} \begin{bmatrix} 2 + i & 0 \\ 0 & 2 - i \end{bmatrix} \begin{bmatrix} 0.5 & 0.5i \\ 0.5 & -0.5i \end{bmatrix}$

## Connection to Stretch Direction

> Complex eigenvalues signify a combination of rotation and scaling in the plane defined by the complex conjugate pair of eigenvectors. The magnitude of the complex eigenvalue still represents scaling, but the angle (argument) of the eigenvalue in the complex plane determines the angle of rotation. Thus, complex eigenvalues don't correspond to simple stretching or stretch directions.

### Eigenvalues and Stretching

Real eigenvalues directly correspond to stretching (or compressing) along the direction of their associated eigenvectors. The magnitude of the eigenvalue tells you the factor by which the stretching occurs.

### Complex Eigenvalues and Rotation

Complex eigenvalues, on the other hand, don't correspond to simple stretching. Instead, they signify a combination of rotation and scaling in the plane defined by the complex conjugate pair of eigenvectors. The magnitude of the complex eigenvalue still represents scaling, but the angle (argument) of the eigenvalue in the complex plane determines the angle of rotation.

### Example:

Consider the matrix:

$A = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$

This matrix represents a 90-degree rotation in the plane. 

Its eigenvalues are i and -i. 

You can see there's no direction in which a vector is simply stretched or compressed by this transformation; instead, all vectors are rotated.



