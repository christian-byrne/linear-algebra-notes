
classdef Matrix

  properties
    matrix
    rank_
    nullity_
    determinant_
    inverse_
  end

  methods

    % Constructor
    function self = Matrix(matrix)
      self.matrix = matrix;

      % Initialize all properties
      self.rank_ = rank(matrix);
      self.nullity_ = size(null(matrix), 2);

      self.determinant_ = det(matrix);
      self.inverse_ = inv(matrix);
    end

    % Getter for rank
    function rank_ = get_rank(self)
      rank_ = self.rank_;
    end

    % Getter for nullity
    function nullity_ = get_nullity(self)
      nullity_ = self.nullity_;
    end


    function display_all_props(self)
      disp("Matrix:");
      disp(self.matrix);
      disp("Rank:");
      disp(self.rank_);
      disp("Nullity:");
      disp(self.nullity_);
      disp("Determinant:");
      disp(self.determinant_);
      disp("Inverse:");
      disp(self.inverse_);
    end
  end

end