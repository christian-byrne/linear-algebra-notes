clear;
clc;
format rat;


syms x;

expr = x^2 - 4*x+4;
expr_2 = x^2 - 2*x -3;

r = expand(expr * expr_2);

roots(r);


A = [
    2 0 2;
    0 2 2;
    2 2 0;
    ];

B = [
    6 0 0;
    0 1 0;
    0 0 1;
    ];

charpoly(A);


roots(poly(A));


[V, D] = eig(A)