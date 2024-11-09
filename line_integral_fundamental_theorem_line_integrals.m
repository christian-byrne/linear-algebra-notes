syms x y z;

% Define the function f(x, y, z)
f = x*y^3 + x^2 - 2*z*y;

% Calculate the gradient of f
F = gradient(f, [x, y, z]);

% Define the endpoints
start_point = [1, 1, 2];
end_point = [3, 17, 2];

% Evaluate f at the endpoints
f_start = subs(f, [x, y, z], start_point);
f_end = subs(f, [x, y, z], end_point);

% Compute the line integral using FTLI
line_integral = f_end - f_start;
disp('The value of the line integral is:');
disp(line_integral);
