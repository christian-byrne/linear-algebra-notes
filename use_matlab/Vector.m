classdef Vector

    properties
        components
        dims
        coefficient
        field
        verbose
    end

    methods (Static, Access = private)

        % -------------------------- Manual Type Checking -------------------------

        function assert_matrix_like(vector, error_msg)

            if nargin < 2
                error_msg = '';
            end

            vector_type = class(vector);
            assert( ...
                vector_type == "Vector" ...
                || vector_type == "Matrix", ...
                "TypeError: Expected a vector or matrix.\n" + error_msg ...
            );
        end

        function assert_shape_match(vector1, vector2, error_msg)

            if nargin < 3
                error_msg = '';
            end

            assert(vector1.dims == vector2.dims, ...
                "ShapeMismatch: Vectors must have the same dimensions.\n" + error_msg ...
            );
        end

    end

    methods (Access = private)

        function bool = is_array_type__(self, unknown)
            bool = isequal(class(self), class(unknown)) || isnumeric(unknown) && ~isscalar(unknown);
        end

        function log__(self, message)

            if self.verbose
                disp(message);
            end

        end

        function rational_components = to_rational__(self)
            rational_components = arrayfun( ...
                @(component) rat(component), ...
                self.components, ...
                "UniformOutput", false ...
            );
        end

    end

    methods (Static)

        function zero_vector = get_zero_vector(dims)
            zero_vector = Vector(zeros(1, dims));
        end

        function unit_vector = get_unit_vector(dims, index)
            unit_vector = Vector(zeros(1, dims));
            unit_vector.components(index) = 1;
        end

        function random_vector = get_random_vector(dims)
            random_vector = Vector(rand(1, dims));
        end

    end

    methods

        function self = Vector(components, verbose)

            if nargin > 0
                self.components = components;
                self.dims = length(components);
            end

            if nargin > 1
                self.verbose = verbose;
            else
                self.verbose = false;
            end

        end

        % -------------------------- Geometric methods -------------------------

        function projection = project(self, onto)

            Vector.assert_matrix_like(onto, 'Cannot project onto a non-vector or non-matrix.');
            Vector.assert_shape_match(self, onto, 'Cannot project vectors of different dimensions.');
            assert(~onto.is_zero_vector(), 'DivideByZero: Cannot project onto the zero vector.');

            %{
                NOTE:
                Operator overloading is not commutative:
                onto * coefficient_ is caught by onto.mtimes.
                coefficient_ * onto is caught by double.mtimes.
            %}

            coefficient_ = (self * onto) / (onto * onto);
            projection = onto * coefficient_;

        end

        function orthogonalized = orthogonalize(self, onto)

            if ~self.is_orthogonal_to(onto)
                orthogonalized = self - self.project(onto);
            else
                orthogonalized = self;
            end

        end

        function normal_vector = normal_vector(self)

            if self.dims == 2
                normal_vector = Vector([self.components(2), -self.components(1)]);
            else
                normal_vector = 'This method only works for 2D vectors';
            end

        end

        function directionVector = direction_vector(self)
            directionVector = self * (1 / norm(self));
        end

        % -------------------------- Comparison methods -------------------------

        function distance = distance_to(self, other)

            if isa(other, "Vector")
                distance = self.distance_to_other_vector(other);
            elseif is_array_type__(other)
                distance = self.distance_to_other_vector(Vector(other));
            else
                error('Distance defined only for vectors and arrays.');
            end

        end

        function distance = distance_to_other_vector(self, other)
            assert(norm(self - other) == norm(other - self), 'Distance is not symmetric.')
            distance = norm(self - other);
        end

        function bool = is_parallel_to(self, other)
            bool = self.is_zero_vector() ...
                || other.is_zero_vector() ...
                || self.angle_between(other) == 0;
        end

        function angle = angle_between(self, other)
            theta = (self * other) / (norm(self) * norm(other));
            angle = acos(theta);
        end

        function bool = is_orthogonal_to(self, other)
            bool = self.is_zero_vector() ...
                || other.is_zero_vector() ...
                || self * other == 0;
        end

        % ------------------------------ Printing ------------------------------

        function disp(self, varargin)
            p = inputParser;
            addOptional(p, 'repr', false);
            addOptional(p, 'rational', true);

            parse(p, varargin{:});

            if p.Results.repr == true
                disp(self)
            elseif p.Results.rational == true
                format rat
                disp(self.components)
            else
                disp(self.components)
            end

        end

        % -------------------------- Operator Overload -------------------------

        function negated = uminus(self)
            negated = Vector(-self.components);
        end

        function bool = ne(self, other)
            bool = ~isequal(self.components, other.components);
        end

        function bool = eq(self, other)
            bool = isequal(self.components, other.components);
        end

        function sum_ = plus(self, other)

            if isscalar(other)
                sum_ = Vector(self.components + other);
            else
                self.assert_matrix_like(other);
                self.assert_shape_match(self, other);
                sum_ = Vector(self.components + other.components);
            end

        end

        function difference = minus(self, other)
            difference = self + other * -1;
        end

        function product = mtimes(self, other)

            if isnumeric(other)
                product = scalar_multiply(self, other);
            else
                self.assert_matrix_like(other);
                self.assert_shape_match(self, other);
                product = dot_product(self, other);
            end

        end

        function product = scalar_multiply(self, scalar)
            product = Vector(arrayfun(@(x) scalar * x, self.components));
        end

        function product = dot_product(self, other)
            result = 0;

            for i = 1:self.dims
                result = result + self.components(i) * other.components(i);
            end

            product = result;
        end

        % -------------------------- Utility methods --------------------------

        % -------------------------- Property Getters --------------------------

        function length = norm(self)
            length = sqrt(self * self);
        end

        function bool = is_zero_vector(self, additive_identity)

            if nargin > 1
                bool = all(self.components == additive_identity);
            else
                bool = all(self.components == 0);
            end

        end

        function bool = is_scalar(self)
            bool = self.dims == 1;
        end

        function bool = is_vector(self)
            bool = self.dims > 1;
        end

    end

end
