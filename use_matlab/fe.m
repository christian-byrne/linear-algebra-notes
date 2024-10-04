clear;
clc;
format rat;
syms x;
syms y;
syms z;

% Problem 1

U = [
    1 -4;
    3 0;
    ];

V = [
    1 0;
    2 5;
    ];

W = [
    1 0;
    1 0;
    ]


A = [
    1 -4 3 0 0;
    1 0 2 5 0;
    1 1 0 0 0;
    ];

rref(A)

clear

% Problem 2

A = [
    1 0 2;
    -1 2 0;
    0 1 3;
    ];

A_inv = inv(A)

r = A_inv * [10 5 -3]'

clear

% Problem 3

coefficients = [
    1 0;
    0 1;
    2 1;
    ];

b = [0 0 1]';

lsqminnorm(coefficients, b)

clear

% Problem 4

A = [
    2 0 0 3 1 2;
    1 1 0 2 2 1;
    1 1 1 1 3 3;
    ];

rref(A)

% The question is whether you it's allowable to transpose and infer pivot
% cols from pivot rows - and whether it's allowable to state the basis as
% the standard basis, rather than the one consisting of columns that are
% elements of A specifically.

rank_A = rank(A)
dims_A = size(A, 2)
null_A = size(null(A), 2)

clear

% Problem 5

B = [
    2 0 1;
    0 1 3;
    1 0 1;
    ];

B_inv = inv(B)

system = [
    2 0 1;
    0 1 3;
    1 0 1;
    ];

constants = [1 2 3]';

B_inv * constants

clear

% Problem 6

C = [
    2 0 3;
    0 0 0;
    -3 0 2;
    ];

charpoly_C = charpoly(C)

eigengvalues_C = eig(C)

svd_C = svd(C)

Ct_times_C = transpose(C) * C

clear

% Problem 7 

input = [
    1 0 0;
    0 3 2;
    0 0 -1;
    ];

output = [
    1 3 3;
    2 -9 8;
    1 6 6;
    ];

inv_input = inv(input)

T = output * inv_input

clear

% 8.a

C = [
    1 2 0;
    2 0 -5;
    ];

A = [1 -3 4]';

CA = C * A

clear

% 8.d

P = [
    1 3;
    5 -1;
    ];

x = [2 -2]';

P_x = P * x 

clear

% 9

