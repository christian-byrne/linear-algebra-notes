clear;
clc;
%format rat;
syms x;
syms y;
syms z;

% Problem 1

i = [1 0 0]';
j = [0 1 0]';
k = [0 0 1]';

v = [3 -1 7]';
w = [1 -1 -5]';

% Dot and Cross product of v and w
dot_product_vw = dot(v, w);
cross_product_vw =cross(v, w);
cross_product_wv =cross(w, v);

% Magnitude (length)
magnitude_v = norm(v);
magnitude_w = norm(w);

% Unit vector
unit_vector_of_v = (1 / magnitude_v) * v;
unit_vector_of_w = (1 / magnitude_w) * w;

% Vector of new_length parallel to v
new_length = 2;
parallel_v_new_len = unit_vector_of_v * new_length;
parallel_w_new_len = unit_vector_of_w * new_length;

% Angle between vw. cos(theta) = vw/||v|| * ||w||
angle_between_vw = acos(dot_product_vw / (magnitude_w * magnitude_v));
angle_between_vw_degress = angle_between_vw * (180/pi);

% Vector perpindicular
function proj = vector_projection(a, b)
    % Projects vector a onto vector b
    proj = (dot(a, b) / dot(b, b)) * b;
end

perp_vector_v = v - vector_projection(v, w);
perp_vector_w = w - vector_projection(w, v);

P = [1 4 2]';
Q = [0 6 3]';
R = [2 -3 3]';

RQ = Q - R;
QR = R - Q;
PQ = Q - P;

norm(RQ);

PQ + QR;

b = [-2 5 -3]';
norm(b);

vv = [3 -1 7]';
ww = [1 -1 -5]';

dot(vv, ww);

A = [2 3 -5]';
B = [2 -3 -1]';
C = [4 6 -2]';
D = [2 3 1]';
E = [2 3 -1]';
F = [1 1 1]';

ab = cross(A, B)
af = cross(A, F)
de = cross(D, E)
ce = cross(C, E)
bf = cross(B, F)
bc = cross(B, C)

a = [3 11/5 -4]';
b = [-1 5 2]';
dot(a, b)

v1 = [2 -4 5]';
v2 = [3 -2 2]';
dot(v1, v2)