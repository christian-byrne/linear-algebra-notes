%  Code for problem 1: 
%------------------------------------------------------------------
% Create the variable matrix K.
K = [
  1 0 5 0;
  2 0 -1 0;
  1 1 0 2;
  0 2 0 1;
];

% Create a constant vector k.
k = [13 4 2 -3]';

% Create an augmented matrix [K | k], call it augKk.
augKk = [K k];

% Find and display RREF for augKk.
format rat
rref_for_augKk = rref(augKk);


%  Code for problem 2: 
%------------------------------------------------------------------
% Create the variable matrix A.
A = [
  1 2 1;
  0 1 -3;
  0 1 -2;
];

% Find the display the inverse of A.
A_inv = inv(A)

% Create the constant vector b.
b = [-7 1 8]';

% Compute $$A^{-1}b$$.
xyz = A_inv * b;


% Create the matrix M.
M = [
  3 0 -1;
  1 0 3;
  5 2 -7;
];

% Find and display the determinant of M.
det_M = det(M)