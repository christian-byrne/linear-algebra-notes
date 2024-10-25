% MATLAB script to visualize r(t) and r(-t) over a constrained domain

% Define the domain for t
t = linspace(1, 2, 100);  % t ranges from 1 to 2

% Define r(t) = [0, 0, 0] + t * [1, 1, 1]
r_t = [t; t; t];  % Each row corresponds to x, y, z components

% Define r(-t) for the same range of t values
r_neg_t = [-t; -t; -t];  % Each row corresponds to x, y, z components

% Plotting r(t)
figure;
plot3(r_t(1, :), r_t(2, :), r_t(3, :), 'b', 'LineWidth', 2);
hold on;

% Plotting r(-t)
plot3(r_neg_t(1, :), r_neg_t(2, :), r_neg_t(3, :), 'r--', 'LineWidth', 2);

% Mark start and end points for clarity
plot3(r_t(1, 1), r_t(2, 1), r_t(3, 1), 'bo', 'MarkerFaceColor', 'b'); % Start of r(t)
plot3(r_t(1, end), r_t(2, end), r_t(3, end), 'bs', 'MarkerFaceColor', 'b'); % End of r(t)

plot3(r_neg_t(1, 1), r_neg_t(2, 1), r_neg_t(3, 1), 'ro', 'MarkerFaceColor', 'r'); % Start of r(-t)
plot3(r_neg_t(1, end), r_neg_t(2, end), r_neg_t(3, end), 'rs', 'MarkerFaceColor', 'r'); % End of r(-t)

% Add labels and legend
xlabel('X');
ylabel('Y');
zlabel('Z');
legend('r(t)', 'r(-t)', 'Location', 'best');
title('Comparison of r(t) and r(-t) with constrained t domain');
grid on;
view(3);
hold off;
