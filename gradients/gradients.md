
## Gradient

The gradient of a function $f(x, y)$ is:

$$
\nabla f = \begin{bmatrix} f_x \\ f_y \end{bmatrix}
$$

Where:

- $f_x$ is the partial derivative of $f$ with respect to $x$.
- $f_y$ is the partial derivative of $f$ with respect to $y$.
- $\nabla f$ is the gradient of $f$.
- The gradient is a vector that points in the direction of the greatest increase of the function.
- The magnitude of the gradient is the rate of change of the function in that direction.
- The gradient is always orthogonal to the level curves of the function.


### Gradient at a Point

The gradient of a function $f(x, y)$ at a point $(x_0, y_0)$ is:

$$
\nabla f(x_0, y_0) = \begin{bmatrix} f_x(x_0, y_0) \\ f_y(x_0, y_0) \end{bmatrix}
$$


### Differential $df$ from Gradient

The differential $df$ of a function $f(x, y)$ is:

$$
df = \nabla f \cdot d\mathbf{r}
$$

Where:

- $\nabla f$ is the gradient of $f$.
- $d\mathbf{r}$ is the differential of the position vector.


The differential of the position vector $d\mathbf{r}$ is:

$$
d\mathbf{r} = \begin{bmatrix} dx \\ dy \end{bmatrix}
$$

$dx$ is found by taking the derivative of the x-component of the position vector with respect to $t$ and multiplying by $dt$.

$dy$ is found by taking the derivative of the y-component of the position vector with respect to $t$ and multiplying by $dt$.

**Example**:

For the grad $f = 6y \vec{i} + 9x \vec{j}$, find the differential $df$:

$$
df = \nabla f \cdot d\mathbf{r} = (6y \vec{i} + 9x \vec{j}) \cdot (dx \vec{i} + dy \vec{j})
$$

$$
df = 6y dx + 9x dy
$$

**Example**:

Find grad $f$ from the differential $df = 3x dx + 4y dy$:

$$
\nabla f = \begin{bmatrix} 3x \\ 4y \end{bmatrix}
$$

