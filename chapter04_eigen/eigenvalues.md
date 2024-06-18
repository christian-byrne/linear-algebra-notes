
# Complex Eigenvalues

## Converting to Polar Form

$a + bi$

$r = \sqrt{a^2 + b^2}$

$\theta = \arctan{\frac{b}{a}}$


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


