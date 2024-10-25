function isParallel = check_parallel(v1, v2)
    % Function to check if two vectors are parallel
    % Input: v1 and v2 are vectors (can be 2D or 3D)
    % Output: isParallel is true if the vectors are parallel, false otherwise

    % Check if the vectors have the same direction using cross product (for 3D vectors)
    if length(v1) == 3 && length(v2) == 3
        cross_product = cross(v1, v2);
        isParallel = norm(cross_product) < 1e-10; % If the cross product is approximately 0, vectors are parallel
    else
        % For 2D or other dimensions, use the ratio method (dot product for 2D)
        ratio = v1 ./ v2;  % Element-wise division
        isParallel = all(abs(ratio - ratio(1)) < 1e-10); % Check if all ratios are the same
    end
end


v1a = [6, 2]'
v1b = [3, 2]'

dot(v1a, v1b)
v1_parallel = check_parallel(v1a, v1b)


v2a = [2, -5]'
v2b = [-6, 15]'

dot(v2a, v2b)
v2_parallel = check_parallel(v2a, v2b)

v3a = [16, 0, -8]'
v3b = [-2, 0, 1]'

dot(v3a, v3b)
v3_parallel = check_parallel(v3a, v3b)

v4a = [2, -10]'
v4b = [5, 1]'

dot(v4a, v4b)
v4_parallel = check_parallel(v4a, v4b)