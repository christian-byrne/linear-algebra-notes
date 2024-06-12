
clear;
clc;

test_matrix = Matrix([1, 0; 0, 1]);

before = Matrix([1, 0, 0; 0, 1, 0; 0, 0, 1]');
after = Matrix([1, 0, 0; 1, 1, 0; 1, 1, 1]');

LinearTransformation(before, after)...
.get_transformation_matrix()...
.display_all_props()
