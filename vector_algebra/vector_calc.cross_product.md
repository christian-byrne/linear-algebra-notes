
## Cross Product

### Definition:

$$
\mathbf{a} \times \mathbf{b} = \begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
a_1 & a_2 & a_3 \\
b_1 & b_2 & b_3
\end{vmatrix} = \left( a_2b_3 - a_3b_2 \right) \mathbf{i} - \left( a_1b_3 - a_3b_1 \right) \mathbf{j} + \left( a_1b_2 - a_2b_1 \right) \mathbf{k}
$$

- $\mathbf{i}$, $\mathbf{j}$, and $\mathbf{k}$ are unit vectors in the x, y, and z directions, respectively.
- The result is $\in \mathbb{R}^3$.
- The result is orthogonal to both $\mathbf{a}$ and $\mathbf{b}$.
- The direction of the result is determined by the right-hand rule (normal vector $\mathbf{n}$ to the plane formed by $\mathbf{a}$ and $\mathbf{b}$).



### Corrolaries:


$$
\mathbf{i} \times \mathbf{j} = \mathbf{k}
$$


$$
\mathbf{i} \times \mathbf{k} = -\mathbf{j}
$$


$$
\mathbf{j} \times \mathbf{i} = -\mathbf{k}
$$


$$
\mathbf{j} \times \mathbf{k} = \mathbf{i}
$$


- When the result is zero:
  - $\mathbf{a} \times \mathbf{a} = \mathbf{0}$
  - $\mathbf{a} \times \mathbf{b} = \mathbf{0}$ if $\mathbf{a}$ and $\mathbf{b}$ are parallel or anti-parallel ($\theta = 0$ or $\theta = \pi$).
  - $\mathbf{a} \times \mathbf{b} = \mathbf{0}$ if $\mathbf{a}$ and $\mathbf{b}$ are orthogonal.
  - $\mathbf{a} \times \mathbf{b} = \mathbf{0}$ if $\mathbf{a}$ and $\mathbf{b}$ are linearly dependent.
- Relationship to Parallelogram:
  - $\mathbf{a} \times \mathbf{b} \perp$ to parallelogram formed by $\mathbf{a}$ and $\mathbf{b}$.
  - $A_{\text{parallelogram}} =$
    - $b * h =$
    - $||\mathbf{a} \times \mathbf{b}|| =$
    - $||\mathbf{a}|| ||\mathbf{b}|| \sin(\theta) =$ 
    - The area of the parallelogram formed by $\mathbf{a}$ and $\mathbf{b}$.
- Relationship to Triangle:
  - $\mathbf{a} \times \mathbf{b} \perp$ to triangle formed by $\mathbf{a}$ and $\mathbf{b}$.
  - $A_{\text{triangle}} = \frac{1}{2} A_{\text{parallelogram}} = \frac{1}{2} ||\mathbf{a} \times \mathbf{b}||$
- With normal vector:
  - $(\mathbf{a} \times \mathbf{b}) \parallel \mathbf{n}$, where $\mathbf{n}$ is the normal vector to the plane formed by $\mathbf{a}$ and $\mathbf{b}$.
  - $\mathbf{a} \times \mathbf{b} = ||\mathbf{a} \times \mathbf{b}|| \mathbf{n}$, where $\mathbf{n}$ is the normal vector to the plane formed by $\mathbf{a}$ and $\mathbf{b}$.

### Field Properties:

- $\mathbf{a} \times \mathbf{b} = -\mathbf{b} \times \mathbf{a}$
- **Associative**:
  - $\mathbf{a} \times (\mathbf{b} + \mathbf{c}) = \mathbf{a} \times \mathbf{b} + \mathbf{a} \times \mathbf{c}$
  - $(\lambda \mathbf{a}) \times \mathbf{b} = \lambda (\mathbf{a} \times \mathbf{b}) = \mathbf{a} \times (\lambda \mathbf{b})$
- **Distributive**:
  - $\mathbf{a} \times (\mathbf{b} + \mathbf{c}) = \mathbf{a} \times \mathbf{b} + \mathbf{a} \times \mathbf{c}$
- **Scalar Multiplication**:
  - $(\lambda \mathbf{a}) \times \mathbf{b} = \lambda (\mathbf{a} \times \mathbf{b}) = \mathbf{a} \times (\lambda \mathbf{b})$
