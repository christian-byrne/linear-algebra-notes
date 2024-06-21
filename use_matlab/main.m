clear;
clc;
format rat;
syms x;
syms y;
syms z;

expr = x^2 - 4*x+4;
expr_2 = x^2 - 2*x -3;
r = expand(expr * expr_2);
roots(r);


A = [
    0 0 1;
    1 0 0;
    0 1 0;
    ];

A_characteristic_polynomial = charpoly(A)
A_eigenvalues = roots(poly(A))
[A_eigenvectors, A_diagonal] = eig(A)

A_svd = svd(A)

A_eigenvectors * A_diagonal * inv(A_eigenvectors)

diagonal_1_1 = A_diagonal(1, 1);
diagonal_1_2 = A_diagonal(1, 1);
diagonal_2_1 = A_diagonal(2, 1);
diagonal_2_2 = A_diagonal(2, 2);

expr_3 = -x^3 + 1
roots(expr_3)

B = [
    3 0 2;
    0 1 0;
    0 2 -2;
    ];

C = [
    1 2/5 2/5;
    0 1/3 0;
    0 -2/15 1/5;
    ];

xx = C * B * inv(C)
rref(xx)