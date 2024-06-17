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
    1 1 1;
    0 -1 0;
    0 0 -1;
    ];

charpoly(A);


roots(poly(A));


[V, D] = eig(B);

C = [
    -1/2 -1/2 1;
    1 0 0;
    0 1 0;
    ];

C_inv = inv(C);

matrix_m = [
    -1 0 0;
    0 -1 0;
    0 0 1;
    ];

my_result = C * matrix_m^2027 * C_inv;

matrix_to_compute_power = [
    1 1 1;
    0 -1 0;
    0 0 -1;
    ];

[mtcp_p, mtcp_d] = eig(matrix_to_compute_power);

matrix_to_compute_power^2027;


ex = [
    -1 1 -1/2;
    1 1 -1/2;
    0 1 1;
    ];

inv(ex);

elipse_example = [
    sqrt(3)/2 1;
    -1/2 sqrt(3);
    ];

[elipse_v, elipse_d] = eig(elipse_example);

disp(elipse_d)

elipse_d(1, 1)


sqrt_3 = sqrt(3)