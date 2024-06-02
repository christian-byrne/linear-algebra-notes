

### Row Reduction


#### Row Operations

![Row Operations](./../chapter01-vectors/pictures/Selection_009.png)

A row operation is an operation that can be performed on a matrix that will not change the solution set of the matrix. There are three types of row operations:
- **Type 1 - Cosmetic Scaling**: Multiply a row by a non-zero scalar
  - $3R_2 \rightarrow R_2$ 
- **Type 2 - Row Swap**: Swap two rows
  - $R_1 \leftrightarrow R_2$
- **Type 3 - Plane Pivot**: Add a multiple of one row to another row
  - $R_1 + 2R_2 \rightarrow R_1$
- If you replace a row, the linear combination that you replace it with should contain that row or a multiple of that row


> Our goal with row operations is to take a set of generators and replace them with an orthogonal set that still passes through the same points. This is done by taking the first generator and subtracting off the projection of the second generator onto the first. This will give us a new generator that is orthogonal to the first. We can then repeat this process for the remaining generators.
 

![alt text](../chapter01-vectors/pictures/row-reduction-simple.png)

![alt text](../chapter01-vectors/pictures/row-reduction-simple-02.png)

#### Row Echelon Form

![alt text](../chapter01-vectors/pictures/row-echelon-form.jpg)

- All zero rows are at the bottom of the matrix
- The leading entry of each row is to the right of the leading entry of the row above it
- All entires below a leading entry are zero

> In echelon form, any variable without a leading entry is a free variable


#### Reduced Row Echelon Form (RREF)

- It is in row echelon form
- The leading entry of each row is the only non-zero entry in its column


### Orthogonality

Two vectors are orthogonal if their dot product is zero. 

- **Orthogonal Set**: A set of vectors is orthogonal if every pair of vectors in the set is orthogonal
- **Orthogonal Basis**: A basis is orthogonal if it is an orthogonal set and it spans the space
- **Orthogonal Matrix**: A matrix is orthogonal if its columns form an orthogonal basis

### Projections

**Projection**: The projection of a vector `v` onto a vector `u` is the vector that is the scalar multiple of `u` that is closest to `v`

**Projection Formula**: The projection of a vector `v` onto a vector `u` is given by the formula:

> $proj_u(v) = \frac{v \cdot u}{u \cdot u} \cdot u$ 

### Generators and Spans

- **Generator**: A generator is a vector that is used to generate a space
- **Span**: The span of a set of vectors is the set of all linear combinations of the vectors

### Vectors

- **Subspace**: A subspace is a subset of a vector space that is itself a vector space
- **Vector Space**: A vector space is a set of vectors that is closed under addition and scalar multiplication
- **Zero Vector**: The zero vector is the vector that is the additive identity in a vector space

#### Addition and Multiplication (Scalar)

![alt text](../chapter01-vectors/pictures/vectors-addition-scaling-multiplication.png)

### Parametric Form

[Interactive Textbook](https://textbooks.math.gatech.edu/ila/parametric-form.html)

![alt text](../chapter01-vectors/pictures/vectors-intrinsic-vs-extrinsic.png)

![alt text](../chapter01-vectors/pictures/parametric-form.png)

### Linear Independence



![alt text](../chapter01-vectors/pictures/vectors-spans-linear-combinations-definitions.png)


#### Free Variables

- Take the total number of dimensions, then subtract the number of free variables, the number of dimensions left determines the shape of the intersection (solution set)
  - there are 2 bound variables then the intersection is a line
  - if there are 1 bound variable, then the intersection is a point, 
- **Free Variable**: A free variable is a variable that does not have a leading entry in a matrix in row echelon form
- **Bound Variable**: A bound variable is a variable that has a leading entry in a matrix in row echelon form
- **Pivot Variable**: A pivot variable is a variable that corresponds to a leading entry in a matrix in row echelon form
- **Dependent Variable**: A dependent variable is a variable that can be expressed in terms of the free variables
- **Independent Variable**: An independent variable is a variable that cannot be expressed in terms of the free variables
- **Rank**: The rank of a matrix is the number of pivot variables in the matrix
- **Nullity**: The nullity of a matrix is the number of free variables in the matrix
- **Rank-Nullity Theorem**: The rank-nullity theorem states that the rank of a matrix plus the nullity of a matrix is equal to the number of columns in the matrix
- **Linearly Independent**: A set of vectors is linearly independent if no vector in the set can be expressed as a linear combination of the other vectors in the set
- **Linearly Dependent**: A set of vectors is linearly dependent if at least one vector in the set can be expressed as a linear combination of the other vectors in the set
- **Basis**: A basis is a set of vectors that is linearly independent and spans the space
- **Dimension**: The dimension of a space is the number of vectors in a basis for the space


### Homogeneity Trick/Procedure

![alt text](../chapter01-vectors/pictures/homogeneity-trick.png)

![alt text](../chapter01-vectors/pictures/homogeneity-trick-example01.png)


