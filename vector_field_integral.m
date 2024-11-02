% Define the function F along the path y = x^2
F1 = @(t) 24 .* t;                           % x-component of F along the path
F2 = @(t) exp(t.^2) - 6 .* sin(t.^2);        % y-component of F along the path

% Define the integrand F · dr along the path
integrand = @(t) F1(t) .* 1 + F2(t) .* (2 .* t); % (F · dr) = F1*dx/dt + F2*dy/dt

% Integrate from t = 0 to t = 1
result = integral(integrand, 0, 1);

% Calculate the expected result using the expression 11 + e + 6 * (1 - cos(1))
expected_result = 5 + exp(1) + 6 * cos(1);

% Display the results
disp('The value of the line integral is:');
disp(result);

disp('The expected result is:');
disp(expected_result);

% Check if the values match within a tolerance
tolerance = 1e-6; % Define a tolerance for comparison
if abs(result - expected_result) < tolerance
    disp('The result matches the expected value.');
else
    disp('The result does NOT match the expected value.');
end
