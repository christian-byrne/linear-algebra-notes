# Partial Derivative

A partial derivative is a derivative of a function of multiple variables with respect to one of those variables, with all other variables held constant.

## Notation

The partial derivative of a function $f(x, y)$ with respect to $x$ is denoted as $\frac{\partial f}{\partial x}$.

The partial derivative of a function $f(x, y, z)$ with respect to $y$ is denoted as $\frac{\partial f}{\partial y}$.

## Definition

The partial derivative of a function $f(x, y)$ with respect to $x$ is defined as

$$
\frac{\partial f}{\partial x} = \lim_{h \to 0} \frac{f(x + h, y) - f(x, y)}{h}
$$

The partial derivative of a function $f(x, y)$ with respect to $y$ is defined as

$$
\frac{\partial f}{\partial y} = \lim_{h \to 0} \frac{f(x, y + h) - f(x, y)}{h}
$$

## Interpretation

The partial derivative $\frac{\partial f}{\partial x}$ gives the rate of change of $f$ with respect to $x$ while holding $y$ constant.

The partial derivative $\frac{\partial f}{\partial y}$ gives the rate of change of $f$ with respect to $y$ while holding $x$ constant.

## Example

Consider the function $f(x, y) = x^2 + y^2$.

The partial derivative of $f$ with respect to $x$ is

$$
\frac{\partial f}{\partial x} = 2x
$$

The partial derivative of $f$ with respect to $y$ is

$$
\frac{\partial f}{\partial y} = 2y
$$

## Chain Rule for Partial Derivatives

Consider the functions 

- $z = g(u, v, w)$
- $u = u(x, y)$
- $v = v(x, y)$
- $w = w(x, y)$

The partial derivative of $z$ with respect to $x$ is

$$
\frac{\partial z}{\partial x} = \frac{\partial g}{\partial u} \frac{\partial u}{\partial x} + \frac{\partial g}{\partial v} \frac{\partial v}{\partial x} + \frac{\partial g}{\partial w} \frac{\partial w}{\partial x}
$$