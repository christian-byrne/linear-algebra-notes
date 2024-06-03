Arithmetic Operators:

Addition (+): plus
Subtraction (-): minus
Multiplication (*): mtimes
Division (/): mrdivide (right division), mldivide (left division)
Comparison Operators:

Equality (==): eq
Inequality (~=): ne
Less Than (<): lt
Greater Than (>): gt
Less Than or Equal (<=): le
Greater Than or Equal (>=): ge
Unary Operators:

Unary Plus (+): uplus
Unary Minus (-): uminus
Indexing Operators:

Assignment (=): subsasgn
Access (()): subsref
Concatenation Operator:

Horizontal Concatenation ([]): horzcat
Vertical Concatenation (semicolon): vertcat
Signature and Function Names
Here's a summary of the signatures and function names for the most common operators:

Arithmetic Operators:

Addition (+): function result = plus(obj1, obj2)
Subtraction (-): function result = minus(obj1, obj2)
Multiplication (*): function result = mtimes(obj1, obj2)
Division (/): function result = mrdivide(obj1, obj2), function result = mldivide(obj1, obj2)
Comparison Operators:

Equality (==): function result = eq(obj1, obj2)
Inequality (~=): function result = ne(obj1, obj2)
Less Than (<): function result = lt(obj1, obj2)
Greater Than (>): function result = gt(obj1, obj2)
Less Than or Equal (<=): function result = le(obj1, obj2)
Greater Than or Equal (>=): function result = ge(obj1, obj2)
Unary Operators:

Unary Plus (+): function result = uplus(obj)
Unary Minus (-): function result = uminus(obj)
Indexing Operators:

Assignment (=): function obj = subsasgn(obj, index, value)
Access (()): function result = subsref(obj, index)
Concatenation Operator:

Horizontal Concatenation ([]): function result = horzcat(obj1, obj2)
Vertical Concatenation (semicolon): function result = vertcat(obj1, obj2)
Notes:
The function names listed above are the names of methods that you define in your class to overload the corresponding operators.
When overloading operators, you implement these methods in your class definition, providing custom behavior for the operators when applied to objects of your class.