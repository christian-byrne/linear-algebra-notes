
# Terminology

We have seen that in $R^n$, it is possible for one vector space to sit inside another one, giving rise to the notion of a ***subspace***.

For example, a plane through the origin in $R^3$ is a subspace of $R^3$.

## Definition

> A subset $W$ of a vector space $V$ is called a ***subspace*** of $V$ if $W$ is a vector space under the operations of addition and scalar multiplication defined in $V$


# Verification of Subspaces


To verify that a subset $W$ of a vector space $V$ is a subspace of $V$, we need to check that the following three conditions hold:

1. The zero vector of $V$ is in $W$
   1. I.e., $0$ is in $W$
2. $W$ is closed under addition
   1. I.e., if $u$ and $v$ are in $W$, then $u + v$ is in $W$
3. $W$ is closed under scalar multiplication
   1. I.e., if $u$ is in $W$ and $c$ is a scalar, then $cu$ is in $W$


$\overline{a_||} \cdot \overline{a_t} = 0$

This is used to represent the dot product of two vectors, where $\overline{a_||}$ is the projection of vector $\overline{a}$ onto the direction of vector $\overline{b}$, and $\overline{a_t}$ is the projection of vector $\overline{a}$ onto the direction perpendicular to vector $\overline{b}$.


# Trivial Subspace

The ***trivial subspace*** of a vector space $V$ is the set containing only the zero vector of $V$.

The trivial subspace is denoted by $\{0\}$.

Another trivial subspace is the vector space itself, $V$.

As a result:

> If $V$ is a vector space, then $\{0\}$ and $V$ are subspaces of $V$
>
> IF $W$ is a subspace of a vector space $V$, then $W$ contains the zero vector of $V$

This fact is consistent with, and analogous to, the fact that lines and planes are subspaces of $R^3$ if and only if they contain the origin.

The requirement that every subspace must contain $0$ is useful in showing that a given set is *not* a subspace.


