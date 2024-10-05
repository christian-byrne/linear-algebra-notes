

## Interpretation of Double Integrals

If $f > 0$, then $\int_R f \, dA$ gives the volume under the graph of $f$ above the region $R$ in the $xy$-plane. 

If $f < 0$, then $\int_R f \, dA$ gives the negative of the volume under the graph of $f$ above the region $R$ in the $xy$-plane. 

If $f$ changes sign, then $\int_R f \, dA$ gives the difference between the volume above the graph of $f$ and the volume below the graph of $f$ above the region $R$ in the $xy$-plane.

## Average Value of $f$ over $R$

The average value of a function $f$ over a region $R$ is given by

$$
\frac{1}{\text{Area}(R)} \int_R f \, dA
$$

## Determining Units

The area of each infinitesimal rectangle $dA$ is is in `units of x` times `units of y`. 

The differential $dA$ is the product of the differentials $dx$ and $dy$.

For each infinitesimal rectangle $dA$, the value of $f$ is in `(units of x) times (units of y)` times `units of f`.

For example, if $f(x, y)$ measures the density of a material at the point $(x, y)$, then the units of $f$ are mass per unit area. The units of $x$ and $y$ are length. Each infinitesimal rectangle $dA$ has units of area. The units for the integral are then `mass per unit area` times `area`, which is `mass`:

$$
\frac{\text{mass}}{\text{area}} \times \text{area} = \text{mass}
$$


## Iterated Integrals

The double integral of a function $f(x, y)$ over a region $R$ can be computed as an iterated integral:

$$
\int_R f \, dA = \int_{x=a}^{x=b} \int_{y=g(x)}^{y=h(x)} f(x, y) \, dy \, dx
$$

or

$$
\int_R f \, dA = \int_{y=c}^{y=d} \int_{x=p(y)}^{x=q(y)} f(x, y) \, dx \, dy
$$

where $R$ is the region in the $xy$-plane bounded by the curves $y = g(x)$, $y = h(x)$, $x = p(y)$, and $x = q(y)$.

### Bounds of Integration for Iterated Integrals

The bounds of integration for the inner integral are functions of the variable of integration for the outer integral.

For example, if the region $R$ is bounded by the curves $y = g(x)$ and $y = h(x)$, then the bounds of integration for the inner integral are $y = g(x)$ and $y = h(x)$.

If the region $R$ is bounded by the curves $x = p(y)$ and $x = q(y)$, then the bounds of integration for the inner integral are $x = p(y)$ and $x = q(y)$.

