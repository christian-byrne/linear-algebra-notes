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
    0 -2;
    -3 0;
    ];

B = [
    1 1 1;
    0 -1 0;
    0 0 -1;
    ];

A_characteristic_polynomial = charpoly(A)
A_eigenvalues = roots(poly(A))
[A_eigenvectors, A_diagonal] = eig(A)

svd(A)

diagonal_1_1 = A_diagonal(1, 1);
diagonal_1_2 = A_diagonal(1, 1);
diagonal_2_1 = A_diagonal(2, 1);
diagonal_2_2 = A_diagonal(2, 2);

