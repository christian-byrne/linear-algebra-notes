
classdef LinearTransformation

  properties
    before_matrix
    after_matrix
    transformation_matrix
  end

  methods

    % Constructor
    function self = LinearTransformation(before_matrix, after_matrix)
      self.before_matrix = before_matrix;
      self.after_matrix = after_matrix;

      % Initialize all properties
      self.transformation_matrix = after_matrix.matrix * inv(before_matrix.matrix);
    end

    % Getter for transformation_matrix
    function transformation_matrix = get_transformation_matrix(self)
      transformation_matrix = Matrix(self.transformation_matrix);
    end

  end

end