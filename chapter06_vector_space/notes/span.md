

# Terminoloy

## Definition

> If $S = \{v_1, v_2, \ldots, v_n\}$ is a set of vectors in a vector space $V$, then the ***span*** of $S$, denoted by $\text{span}(S)$, is the set of all possible linear combinations of the vectors in $S$.

If $V = \text{span}(S)$, then we say that $S$ ***spans*** $V$ or that $S$ is a ***spanning set*** for $V$ and that $V$ is ***spanned*** by $S$.

## Notation

- The span of a set of vectors $S = \{v_1, v_2, \ldots, v_n\}$ is denoted by $\text{span}(v_1, v_2, \ldots, v_n)$
- The span of a single vector $v$ is denoted by $\text{span}(v)$

## Example

![alt text](pictures/span-example.png)

![alt text](pictures/span-example-2.png)


It is true that $\sin(2x)$ can be written in terms of $\sin(x)$ and $\cos(x)$. For example, we have the double angle formula $\sin(2x) = 2\sin(x)\cos(x)$. However, this is not a *linear* combination of $\sin(x)$ and $\cos(x)$, so $\sin(2x)$ is not in the span of $\sin(x)$ and $\cos(x)$.


# Theorem - Subspace Spanned by a Set of Vectors

> The span of a set of vectors is always a subspace of the vector space in which the vectors reside.
>
> Let $V$ be a vector space and $S = \{v_1, v_2, \ldots, v_n\}$ be a set of vectors in $V$. 
> 
> $\text{span}(v_1, v_2, \ldots, v_n)$ is a subspace of $V$.


# Theorem - Smallest Subspace

> The span of a set of vectors is the smallest subspace of the vector space that contains the vectors.
>
> Let $V$ be a vector space and $S = \{v_1, v_2, \ldots, v_n\}$ be a set of vectors in $V$.
>
> If $W$ is a subspace of $V$ that contains $S$, then $\text{span}(v_1, v_2, \ldots, v_n) \subseteq W$.


