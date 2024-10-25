% Define a grid of points in the x-y plane
[x, y] = meshgrid(-5:1:5, -5:1:5);  % Create a grid of points from -5 to 5 for both x and y

% Define the components of the vector field
u = zeros(size(x));  % No x-component (u) since the vector field is in the y direction
v = y;  % y-component (v) is proportional to the y-coordinate

% Plot the vector field using quiver
figure;
quiver(x, y, u, v, 'b');  % 'b' specifies blue arrows
xlabel('x');
ylabel('y');
title('Vector Field: y \cdot j (Points in the y-direction)');
axis equal;  % Make sure the axes are equally scaled
grid on;

% -----------------------------------------

% Define a grid of points in the x-y plane
[x, y] = meshgrid(-5:1:5, -5:1:5);  % Create a grid of points from -5 to 5 for both x and y

% Define the components of the vector field
u = y;      % x-component (u) is proportional to the y-coordinate
v = -x;     % y-component (v) is proportional to the negative x-coordinate

% Plot the vector field using quiver
figure;
quiver(x, y, u, v, 'r');  % 'r' specifies red arrows
xlabel('x');
ylabel('y');
title('Vector Field: y \cdot i + (-x) \cdot j');
axis equal;  % Make sure the axes are equally scaled
grid on;