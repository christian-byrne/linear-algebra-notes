% Define the vector F
Fx = 2;
Fy = -2;
Fz = 1;

% Calculate the magnitude of F
F_magnitude = sqrt(Fx^2 + Fy^2 + Fz^2);

% Define the length of the line segment and the angle
C_length = 9;
theta = pi / 3;

% Calculate the line integral
line_integral = F_magnitude * C_length * cos(theta);

% Display the result
disp('The value of the line integral is:');
disp(line_integral);

% Expected result for verification
expected_result = 13.5; % Calculated manually in previous answer
disp('Expected result is:');
disp(expected_result);

% Check if the values match
tolerance = 1e-6; % Define a tolerance for comparison
if abs(line_integral - expected_result) < tolerance
    disp('The result matches the expected value.');
else
    disp('The result does NOT match the expected value.');
end
