function wrapped_function = transparency_wrapper(func)

    function varargout = wrapper(varargin)

        if isempty(varargin)
            argStr = '';
        else
            argStr = strjoin(cellfun(@(x) sprintf('''%s''', x), varargin, 'UniformOutput', false), ', ');
        end

        % Evaluate in the base workspace and assign to temporary variable
        newWS = struct();
        temp = evalin('base', func2str(func));
        assignin('base', 'temp', temp);

        % Now call the function handle (variables should persist)
        evalin('base', sprintf('temp(%s);', argStr));

        % Get variables defined within the wrapped function's workspace
        lexical_vars = evalin('base', 'who');

        for i = 1:numel(lexical_vars)
            newWS.(lexical_vars{i}) = evalin('base', lexical_vars{i});
        end

        % Print the variables with their values
        for i = 1:numel(lexical_vars)
            fprintf('New variable: %s = \n', lexical_vars{i});
            disp(newWS.(lexical_vars{i}));
        end

        % Assign the variables to the base workspace
        for i = 1:numel(lexical_vars)
            assignin('base', lexical_vars{i}, newWS.(lexical_vars{i}));
        end

    end

    wrapped_function = @wrapper;
end

function outVars = test_vector_projection()

    vec_a = Vector([4, 2, 1]);
    vec_b = Vector([2, 1, 3]);
    projection = vec_a.project(vec_b);

    outVars = {vec_a, vec_b, projection};

end

x = transparency_wrapper(@test_vector_projection);
x();
