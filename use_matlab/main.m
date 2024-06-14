clear;
clc;
format rat;


syms x;

expr = x^2 - 4*x+4;
expr_2 = x^2 - 2*x -3;

r = expand(expr * expr_2)

roots(r)


A = [
    2 0 3;
    4 -1 4;
    3 0 2;
    ];


charpoly(A)


roots(poly(A))
