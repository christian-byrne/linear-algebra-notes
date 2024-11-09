syms x y;

% Define the vector field G
G1 = 2 * cos(2*x + 3*y);
G2 = 3 * cos(2*x + 3*y);

%% Part A: Determine if G is conservative
% Compute the partial derivatives
dG1_dy = diff(G1, y);
dG2_dx = diff(G2, x);

% Check if the mixed partial derivatives are equal
is_conservative = simplify(dG1_dy - dG2_dx) == 0;

disp('Part A:');
if is_conservative
    disp('G is conservative.');
    % Find the potential function f such that G = grad(f)
    % Integrate G1 with respect to x
    f_x = int(G1, x);
    % Differentiate f_x with respect to y
    f_x_y = diff(f_x, y);
    % Find the term in f that depends only on y by subtracting f_x_y from G2
    g_y = G2 - f_x_y;
    % Integrate g_y with respect to y to get the y-dependent part of f
    f_y = int(g_y, y);
    % The potential function f is:
    f = f_x + f_y;
    disp('Potential function f(x, y) = ');
    disp(simplify(f));
else
    disp('G is not conservative.');
end

%% Part B: Line integral over C1 without parametrizing the curve
if is_conservative
    % C1 endpoints
    A = [0, -pi];
    B = [2, 8];
    C = [5, 12];
    D = [pi/4, 0];
    
    % Evaluate f at each point
    f_A = subs(f, [x, y], A);
    f_B = subs(f, [x, y], B);
    f_C = subs(f, [x, y], C);
    f_D = subs(f, [x, y], D);
    
    % Compute the line integral using FTLI
    integral_C1 = f_D - f_A;
    disp('Part B:');
    disp('The value of the line integral over C1 is:');
    disp(vpa(integral_C1));
else
    disp('Part B: G is not conservative, so FTLI cannot be applied.');
end

%% Part C: Line integral over C2 (ellipse) without parametrizing the curve
disp('Part C:');
if is_conservative
    disp('The integral over a closed path in a conservative field is zero.');
    integral_C2 = 0;
else
    % For a non-conservative field, apply Green's theorem if needed
    % Calculate the curl of G to verify if Green's theorem could be applied
    curl_G = diff(G2, x) - diff(G1, y);
    if simplify(curl_G) == 0
        disp('The field has zero curl, implying path independence.');
        integral_C2 = 0;
    else
        disp('The field is not conservative, and the curl is non-zero.');
        disp('Therefore, Green''s theorem can be applied to find the circulation over the ellipse.');
        
        % Integrate the curl over the region inside C2 (ellipse)
        % Area of the ellipse with axes lengths 5 and 6
        a = 5;
        b = 6;
        area_ellipse = pi * a * b;
        integral_C2 = simplify(curl_G) * area_ellipse;
    end
end

disp('The value of the line integral over C2 is:');
disp(vpa(integral_C2));


syms x y;

% Define M and N
M = 8*y + 6*exp(sqrt(x));
N = 11*x + 5*cos(y^2);

% Compute the partial derivatives for Green's Theorem
dN_dx = diff(N, x);
dM_dy = diff(M, y);

% Define the integrand for Green's Theorem
integrand = dN_dx - dM_dy;

% Set up the bounds of integration
% The region bounded by y = x^2 and x = y^2 can be split as:
% 1. For 0 <= x <= 1, y ranges from x^2 to sqrt(x)

% Perform the double integration
area_integral = int(int(integrand, y, x^2, sqrt(x)), x, 0, 1);

disp('The value of the line integral around C is:');
disp(vpa(area_integral));
