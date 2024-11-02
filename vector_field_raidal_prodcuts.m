% Define the circle's radius and orientation
radius = 1;
theta = linspace(0, -2*pi, 100); % Negative angle for clockwise orientation
x_circle = radius * cos(theta);
y_circle = radius * sin(theta);

% Define grid for plotting vector fields
[x, y] = meshgrid(-2:0.5:2, -2:0.5:2);

% Corrected vector fields based on the description
% (i) Horizontal field, left when x < 0, right when x > 0
F1x = sign(x); % Gives -1 when x < 0, 1 when x > 0
F1y = zeros(size(y));

% (ii) Counterclockwise rotational field
F2x = -y;
F2y = x;

% (iii) Vertical field, up when x < 0, down when x > 0
F3x = zeros(size(x));
F3y = -sign(x);

% (iv) Radial inward field (points toward the origin)
F4x = -x;
F4y = -y;

% Plotting setup
figure;
titles = {'(i) Horizontal field left/right', '(ii) Counterclockwise rotational field', ...
          '(iii) Vertical field up/down', '(iv) Radial inward field'};
fields_x = {F1x, F2x, F3x, F4x};
fields_y = {F1y, F2y, F3y, F4y};

for i = 1:4
    subplot(2, 2, i);
    quiver(x, y, fields_x{i}, fields_y{i}, 'r'); % Plot vector field
    hold on;
    plot(x_circle, y_circle, 'b-', 'LineWidth', 1.5); % Plot clockwise circle
    hold off;
    axis equal;
    xlim([-2, 2]);
    ylim([-2, 2]);
    title(titles{i});
end

% Calculate circulation for each vector field
circulations = zeros(4, 1);
field_functions = {@(x, y) sign(x), @(x, y) 0;    % (i) Horizontal field left/right
                   @(x, y) -y, @(x, y) x;         % (ii) Rotational field
                   @(x, y) 0, @(x, y) -sign(x);   % (iii) Vertical field up/down
                   @(x, y) -x, @(x, y) -y};       % (iv) Radial inward field

for i = 1:4
    Fx = field_functions{i, 1};
    Fy = field_functions{i, 2};
    circulation = 0;
    for j = 1:length(theta) - 1
        % Midpoint of the segment on the circle
        xm = (x_circle(j) + x_circle(j+1)) / 2;
        ym = (y_circle(j) + y_circle(j+1)) / 2;
        
        % Tangent vector along the circle (clockwise direction)
        dx = x_circle(j+1) - x_circle(j);
        dy = y_circle(j+1) - y_circle(j);
        
        % Dot product F · dr for the segment
        dC = Fx(xm, ym) * dx + Fy(xm, ym) * dy;
        circulation = circulation + dC;
    end
    circulations(i) = circulation;
end

% Display results with explicit check for zero circulation
for i = 1:4
    if abs(circulations(i)) < 1e-6  % Use a small tolerance to check for zero
        fprintf('Circulation for field %d is zero.\n', i);
    elseif circulations(i) > 0
        fprintf('Circulation for field %d is positive.\n', i);
    else
        fprintf('Circulation for field %d is negative.\n', i);
    end
end
