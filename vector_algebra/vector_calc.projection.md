
## Projection

The projection of a vector $\overrightarrow{u}$ onto a vector $\overrightarrow{v}$ is the vector that represents the shadow of $\overrightarrow{u}$ onto $\overrightarrow{v}$. The projection of $\overrightarrow{u}$ onto $\overrightarrow{v}$ is found by:

$$\text{proj}_{\overrightarrow{v}} \overrightarrow{u} = \frac{\overrightarrow{u} \cdot \overrightarrow{v}}{\|\overrightarrow{v}\|^2} \overrightarrow{v}$$

### Terminology

Finding the projection of a vector $\overrightarrow{u}$ onto a vector $\overrightarrow{v}$ is the same as finding the component of $\overrightarrow{u}$ in the direction of $\overrightarrow{v}$ (or "the component of $\overrightarrow{u}$ parallel to $\overrightarrow{v}$").


## Orthogonal Vectors

Two vectors are orthogonal if their dot product is 0. This means that the angle between the vectors is 90 degrees.

To find the orthogonal vector to a given vector $\overrightarrow{u}$, find a vector $\overrightarrow{v}$ such that $\overrightarrow{u} \cdot \overrightarrow{v} = 0$.

- **Step 1**: Find the projection of $\overrightarrow{u}$ onto $\overrightarrow{v}$.
  - $\text{proj}_{\overrightarrow{v}} \overrightarrow{u} = \frac{\overrightarrow{u} \cdot \overrightarrow{v}}{\|\overrightarrow{v}\|^2} \overrightarrow{v}$
- **Step 2**: Find the orthogonal vector by subtracting the projection from the original vector.
  - $\overrightarrow{u} - \text{proj}_{\overrightarrow{v}} \overrightarrow{u}$
  - This is the vector that is orthogonal to $\overrightarrow{v}$.

### Terminology

Orthogonalizing $u$ is the same as finding the component of $u$ that is orthogonal/normal/perpendicular to $v$.

> **In Word Problems**: Finding the component of the wind in the direction of the ground = finding the projection of the wind onto the ground. Finding the speed of the wind in the direction of the ground = finding the magnitude of the projection of the wind onto the ground (square root of the sum of the squares of the components of the projection).


## Determining if Vectors are Parallel

Two vectors are parallel if one is a scalar multiple of the other. This means that the vectors are in the same direction, but may have different magnitudes.

To determine if two vectors are parallel, find the scalar $c$ such that $\overrightarrow{u} = c \overrightarrow{v}$.

To find the scalar $c$, set the components of the vectors equal to each other and solve for $c$.

If the vectors are parallel, the scalar $c$ will be the same for all components of the vectors.


## Determining if Angle-Between is Less than 90 Degrees ($\frac{\pi}{2}$)

If $\theta = \cos^{-1}(\frac{\overrightarrow{u} \cdot \overrightarrow{v}}{\|\overrightarrow{u}\| \|\overrightarrow{v}\|})$, then the angle is less than 90 degrees if the value inside the inverse cosine function is positive.

I.e., if $x = \frac{\overrightarrow{u} \cdot \overrightarrow{v}}{\|\overrightarrow{u}\| \|\overrightarrow{v}\|}$, then the angle is less than 90 degrees if $x > 0$.

If $x = 0$, then the angle is 90 degrees exactly.


## Law of Cosines Problems (Triangles Given by Vertices)

If given vertices, you find the length of the sides of the triangle sides by finding the displacement vectors between the vertices. Then, find the magnitudes of the displacement vectors to find the lengths of the sides of the triangle.

It does not matter if you do $A - B$ or $B - A$ to find the displacement vector between two points. The magnitude of the displacement vector will be the same.

Then use the Law of Cosines can be used to find the length of a side of the triangle.

To find angle C (ABC):

$$\cos(C) = \frac{a^2 + b^2 - c^2}{2ab}$$

To find side c:

$$c = \sqrt{a^2 + b^2 - 2ab \cos(C)}$$

To find angle A (BAC):

$$\cos(A) = \frac{b^2 + c^2 - a^2}{2bc}$$

To find side a:

$$a = \sqrt{b^2 + c^2 - 2bc \cos(A)}$$

To find angle B (ABC):

$$\cos(B) = \frac{a^2 + c^2 - b^2}{2ac}$$

To find side b:

$$b = \sqrt{a^2 + c^2 - 2ac \cos(B)}$$
