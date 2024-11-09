% Define the vector field components
Fx = -4;  % x-component of F is constant -4
Fy = 7;   % y-component of F is constant 7

% Define the parameterized line segment from (3, 4) to (8, 15)
t = linspace(0, 1, 100); % Parameter t ranges from 0 to 1
x = 3 + (8 - 3) * t;     % x(t) = 3 + (8 - 3) * t
y = 4 + (15 - 4) * t;    % y(t) = 4 + (15 - 4) * t

% Calculate dx and dy along the line segment
dx = gradient(x, t);
dy = gradient(y, t);

% Compute F · dr along the line segment
F_dot_dr = Fx * dx + Fy * dy;

% Integrate F · dr over t from 0 to 1
line_integral = trapz(t, F_dot_dr); % Numerical integration

% Display the result
disp('The value of the line integral is:');
disp(line_integral);

% Expected result for verification
expected_result = 57; % Calculated manually in the previous answer
disp('Expected result is:');
disp(expected_result);

% Check if the values match
tolerance = 1e-6; % Define a tolerance for comparison
if abs(line_integral - expected_result) < tolerance
    disp('The result matches the expected value.');
else
    disp('The result does NOT match the expected value.');
end
