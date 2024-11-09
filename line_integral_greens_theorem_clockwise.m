% Define the radius of the circle
radius = 10;

% Parameterize the circle (counterclockwise orientation)
theta = linspace(0, 2*pi, 1000); % theta from 0 to 2*pi
x = radius * cos(theta);          % x = 10 * cos(theta)
y = radius * sin(theta);          % y = 10 * sin(theta)

% Define the vector field components
Fx = @(x, y) -y ./ (x.^2 + y.^2).^2;
Fy = @(x, y) x ./ (x.^2 + y.^2).^2;

% Calculate dx and dy along the circle
dx = gradient(x, theta);  % derivative of x with respect to theta
dy = gradient(y, theta);  % derivative of y with respect to theta

% Compute F · dr along the circle
F_dot_dr = Fx(x, y) .* dx + Fy(x, y) .* dy;

% Integrate F · dr over theta from 0 to 2*pi
line_integral = trapz(theta, F_dot_dr); % Numerical integration

% Display the result
disp('The value of the line integral is:');
disp(line_integral);

% Expected result for verification
expected_result = pi / 50;
disp('Expected result is:');
disp(expected_result);

% Check if the values match
tolerance = 1e-6; % Define a tolerance for comparison
if abs(line_integral - expected_result) < tolerance
    disp('The result matches the expected value.');
else
    disp('The result does NOT match the expected value.');
end
