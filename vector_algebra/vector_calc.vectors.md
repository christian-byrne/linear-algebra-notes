

# Vectors

A Vector $\overrightarrow{QP}$ is found by subtracting the initial point from the terminal point:

$$\overrightarrow{QP} = \begin{bmatrix} x_2 - x_1 \\ y_2 - y_1 \end{bmatrix}$$

## Notation

A Vector that is in column vector format:

$$\overrightarrow{u} = \begin{bmatrix} u_1 \\ u_2 \end{bmatrix}$$

Can be represented as an equation by using unit vectors:

$$\overrightarrow{u} = u_1 \hat{i} + u_2 \hat{j}$$

All the operations and application are still the same.

*A displacement vector from point $P$ to point $Q$ is denoted as $\overrightarrow{PQ}$ and found by subtracting $P$ from $Q$ component-wise.*



### Example

If $\overrightarrow{u} = \begin{bmatrix} 3 \\ 4 \end{bmatrix}$, and $\overrightarrow{v} = \begin{bmatrix} 1 \\ 2 \end{bmatrix}$, then:

$$\overrightarrow{u} + \overrightarrow{v} = \begin{bmatrix} 3 \\ 4 \end{bmatrix} + \begin{bmatrix} 1 \\ 2 \end{bmatrix} = \begin{bmatrix} 4 \\ 6 \end{bmatrix}$$

In unit vector notation:

$$\overrightarrow{u} + \overrightarrow{v} = 3 \hat{i} + 4 \hat{j} + 1 \hat{i} + 2 \hat{j} = 4 \hat{i} + 6 \hat{j}$$

## Scalar vs. Vector

- **Scalar**: A single number that represents a quantity and has no direction.
  - Temperature
  - Speed
  - Mass
  - Distance
  - Time
  - Volume
  - Area
- **Vector**: A quantity that has both magnitude and direction.
  - Velocity
  - Acceleration
  - Force
  - Displacement
  - Momentum
  - Weight
  - Electric Field
  - Magnetic Field


## Field Operations

1. **Addition**: $\overrightarrow{u} + \overrightarrow{v} = \begin{bmatrix} u_1 + v_1 \\ u_2 + v_2 \end{bmatrix}$
    1. *Associative*: $(\overrightarrow{u} + \overrightarrow{v}) + \overrightarrow{w} = \overrightarrow{u} + (\overrightarrow{v} + \overrightarrow{w})$
    2. *Commutative*: $\overrightarrow{u} + \overrightarrow{v} = \overrightarrow{v} + \overrightarrow{u}$
    3. *Identity*: $\overrightarrow{u} + \overrightarrow{0} = \overrightarrow{u}$
    4. *Inverse*: $\overrightarrow{u} + (-\overrightarrow{u}) = \overrightarrow{0}$
    5. *Distributive*: $c(\overrightarrow{u} + \overrightarrow{v}) = c \overrightarrow{u} + c \overrightarrow{v}$
2. **Scalar Multiplication**: $c \overrightarrow{u} = \begin{bmatrix} c u_1 \\ c u_2 \end{bmatrix}$
    1. *Associative*: $c(d \overrightarrow{u}) = (cd) \overrightarrow{u}$
    2. *Identity*: $1 \overrightarrow{u} = \overrightarrow{u}$
    3. *Distributive*: $(c + d) \overrightarrow{u} = c \overrightarrow{u} + d \overrightarrow{u}$
    6. *Inverses*: $-1 \overrightarrow{u} = -\overrightarrow{u}$
3. **Dot Product**: $\overrightarrow{u} \cdot \overrightarrow{v} = u_1 v_1 + u_2 v_2$
    1. *Commutative*: $\overrightarrow{u} \cdot \overrightarrow{v} = \overrightarrow{v} \cdot \overrightarrow{u}$
    2. *Distributive*: $\overrightarrow{u} \cdot (\overrightarrow{v} + \overrightarrow{w}) = \overrightarrow{u} \cdot \overrightarrow{v} + \overrightarrow{u} \cdot \overrightarrow{w}$
    3. *Associative*: $(c \overrightarrow{u}) \cdot \overrightarrow{v} = c (\overrightarrow{u} \cdot \overrightarrow{v})$
    4. *Identity*: $\overrightarrow{u} \cdot \overrightarrow{u} = \|\overrightarrow{u}\|^2$
    5. *Orthogonal*: $\overrightarrow{u} \cdot \overrightarrow{v} = 0 \Rightarrow \overrightarrow{u} \perp \overrightarrow{v}$
    6. *Maximum*: $|\overrightarrow{u} \cdot \overrightarrow{v}|$ has a maximum value when $\overrightarrow{u} = \overrightarrow{v}$
    7. *Minimum*: $|\overrightarrow{u} \cdot \overrightarrow{v}|$ has a minimum value when $\overrightarrow{u} = -\overrightarrow{v}$
    6. *Cosine*: $\overrightarrow{u} \cdot \overrightarrow{v} = \|\overrightarrow{u}\| \|\overrightarrow{v}\| \cos(\theta)$
    7. *Projection*: $\text{proj}_{\overrightarrow{v}} \overrightarrow{u} = \frac{\overrightarrow{u} \cdot \overrightarrow{v}}{\|\overrightarrow{v}\|^2} \overrightarrow{v}$
    8. *Perpendicular*: $\overrightarrow{u} = \text{proj}_{\overrightarrow{v}} \overrightarrow{u} + \overrightarrow{u} - \text{proj}_{\overrightarrow{v}} \overrightarrow{u}$ 
    9. *Triangle Inequality*: $\|\overrightarrow{u} + \overrightarrow{v}\| \leq \|\overrightarrow{u}\| + \|\overrightarrow{v}\|$
    10. *Cauchy-Schwarz*: $|\overrightarrow{u} \cdot \overrightarrow{v}| \leq \|\overrightarrow{u}\| \|\overrightarrow{v}\|$ 

![alt text](../pictures/Vector_Addition.svg.png)

## Norm (Magnitude)

The norm of a vector $\overrightarrow{u}$ is the length of the vector:

$$\|\overrightarrow{u}\| = \sqrt{u_1^2 + u_2^2 + \ldots + u_n^2}$$

## Dot Product Formula


$$\overrightarrow{u} \cdot \overrightarrow{v} = \|\overrightarrow{u}\| \|\overrightarrow{v}\| \cos(\theta)$$


Where:

- $\theta =$ the angle between the vectors = 0 if $\overrightarrow{u} = \overrightarrow{v}$
- $||\overrightarrow{u}|| =$ the magnitude of $\overrightarrow{u}$
- $||\overrightarrow{v}|| =$ the magnitude of $\overrightarrow{v}$
- $\overrightarrow{u} \cdot \overrightarrow{v} =$ the dot product of $\overrightarrow{u}$ and $\overrightarrow{v}$

### Angle Between Vectors

The angle between two vectors $\overrightarrow{u}$ and $\overrightarrow{v}$ is directly derived from the dot product formula:

$$\cos(\theta) = \frac{\overrightarrow{u} \cdot \overrightarrow{v}}{\|\overrightarrow{u}\| \|\overrightarrow{v}\|}$$


*NOTE*: Don't forget to convert the angle to degrees if needed. To do this, use the formula:

$$\text{degrees} = \frac{\text{radians}}{\pi} \times 180$$


### Finding Parallel Vector with New Length

- **Step 1**: Normalize the vector by dividing the vector by its magnitude.
  - E.g., $\overrightarrow{u} = \begin{bmatrix} 3 \\ 4 \end{bmatrix}$, then $\overrightarrow{u} = \frac{1}{5} \begin{bmatrix} 3 \\ 4 \end{bmatrix} = \begin{bmatrix} \frac{3}{5} \\ \frac{4}{5} \end{bmatrix}$
- **Step 2**: Multiply the normalized vector by the new length.
  - E.g., $\overrightarrow{u} = \begin{bmatrix} \frac{3}{5} \\ \frac{4}{5} \end{bmatrix}$, then a new vector in same direction with length 9 is $\begin{bmatrix} \frac{3}{5} \\ \frac{4}{5} \end{bmatrix} \times 9 = \begin{bmatrix} \frac{27}{5} \\ \frac{36}{5} \end{bmatrix}$


### Example - Hexagon

The change in y for v is positive, and the change in u is 0. Thus, if the formula for w was u - v, then the change in the y direction would be negative. Thus, the formula for w is v - u. Also can be confirmed by noticing that the change in x switched directions, implying that the term being subtracted from has less change in x than the term being subtracted

![alt text](../pictures/vectors-hexagon.png)



## Resolving Vectors

Resolving a vector into its components is the process of finding the horizontal and vertical components of a vector. This is done by using trigonometry.

### Example

Given a vector with magnitude 60 km/hr and an angle of 30 degrees, find the horizontal and vertical components.

- **Step 1**: Find the horizontal component.
  - $60 \cos(30) = 60 \times \frac{\sqrt{3}}{2} = 30 \sqrt{3}$
  - The horizontal component is $30 \sqrt{3}$ km/hr.
- **Step 2**: Find the vertical component.
  - $60 \sin(30) = 60 \times \frac{1}{2} = 30$
  - The vertical component is 30 km/hr.
- **Step 3**: Write the components as a vector.
  - The vector is $\begin{bmatrix} 30 \sqrt{3} \\ 30 \end{bmatrix}$ km/hr.


### Example - Direction of Plane against Wind

> An airplane is flying at an airspeed of 510 km/hr in a wind blowing at 50 km/hr toward the southeast. In what direction should the plane head to end up going due east


1. Resolve the wind vector into its components.
    - Find the x-component: $\cos(45) = \frac{x}{50} \Rightarrow x = 50 \cos(45) = 50 \times \frac{1}{\sqrt{2}} = \frac{50}{\sqrt{2}}$
    - Find the y-component: $\sin(45) = \frac{y}{50} \Rightarrow y = 50 \sin(45) = 50 \times \frac{1}{\sqrt{2}} = \frac{50}{\sqrt{2}}$
      - Since the wind is blowing toward the southeast, the y-component is negative.
    - Thus, the wind vector is $\begin{bmatrix} \frac{50}{\sqrt{2}} \\ -\frac{50}{\sqrt{2}} \end{bmatrix}$ km/hr.
2. Resolve the airspeed vector into its components, using a variable in place of the angle.
    - Find the x-component: $\cos(\theta) = \frac{x}{510} \Rightarrow x = 510 \cos(\theta)$
    - Find the y-component: $\sin(\theta) = \frac{y}{510} \Rightarrow y = 510 \sin(\theta)$
3. Add the wind vector to the airspeed vector to find the resultant vector.
    - The x-component is $510 \cos(\theta) + \frac{50}{\sqrt{2}}$
    - The y-component is $510 \sin(\theta) - \frac{50}{\sqrt{2}}$
4. Since the plane should end up going due east, the y-component should be 0.
    - $510 \sin(\theta) - \frac{50}{\sqrt{2}} = 0 \Rightarrow 510 \sin(\theta) = \frac{50}{\sqrt{2}} \Rightarrow \sin(\theta) = \frac{50}{510 \sqrt{2}}$
    - $\theta = \sin^{-1}(\frac{50}{510 \sqrt{2}})$
5. While flying at this angle, the plane's speed relative to the ground (x) is found by finding the magnitude of the resultant vector.
    - For the x-component: $510 \cos(\sin^{-1}(\frac{50}{510 \sqrt{2}})) + \frac{50}{\sqrt{2}}$
      - ***PREVIOUS MISTAKE***: Make sure to use the formula for the resultant vector, not the original airspeed vector with theta.
    - For the y-component, since the plane should end up going due east, the y-component should be 0.
    - The magnitude of the resultant vector is $\sqrt{(\text{x-component})^2 + (\text{y-component})^2} = \sqrt{(\text{x-component})^2} = \text{x-component}$


