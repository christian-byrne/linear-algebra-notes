- [Terminology](#terminology)
  - [Notation](#notation)
  - [Necessary Conditions for a Vector Space](#necessary-conditions-for-a-vector-space)
- [Fields and Real Vector Space](#fields-and-real-vector-space)
  - [Vector Space Examples](#vector-space-examples)
    - [Prime Vector Space](#prime-vector-space)
    - [Not-Vector Spaces](#not-vector-spaces)
- [Fundamental Properties of Vector Spaces](#fundamental-properties-of-vector-spaces)
    - [Fundamental Properties of Scalar Multiplication in Vector Spaces](#fundamental-properties-of-scalar-multiplication-in-vector-spaces)

# Terminology

## Notation

- Let $V$ be a set on which two operations, called *addition* and *scalar multiplication* have been defined
  - If $u$ and $v$ are in $V$, the *sum* of $u$ and $v$ is denoted by $u + v$
  - If $c$ is a scalar, the *scalar multiple* of $u$ by $c$ is denoted by $cu$

## Necessary Conditions for a Vector Space

> If the following axioms hold for all $u$, $v$, and $w$ in $V$ and all scalars $c$ and $d$, then $V$ is called a ***vector space*** over the field $F$ and its elements are called ***vectors***


| Description | Axiom |
| --- | --- |
| **Closure under addition** | $u + v$ is in $V$ |
| Commutativity of addition | $u + v = v + u$ |
| Associativity of addition | $(u + v) + w = u + (v + w)$ |
| **Additive identity/Existence of Zero Vector** | There exists an element $0$ in $V$ such that $u + 0 = u$ for all $u$ in $V$ |
| **Additive Inverse** | For each $u$ in $V$, there exists an element $-u$ in $V$ such that $u + (-u) = 0$ |
| **Closure under scalar multiplication** | $cu$ is in $V$ |
| Distributivity of scalar multiplication with respect to vector addition | $c(u + v) = cu + cv$ |
| Distributivity of scalar multiplication with respect to field addition | $(c + d)u = cu + du$ |
| Associativity of scalar multiplication | $c(du) = (cd)u$ |
| Multiplicative identity | $1u = u$ |


# Fields and Real Vector Space

- Scalars can be chosen from any set of numbers in which, roughly speaking, the operations of addition, subtraction, multiplication, and division are defined
- In abstract algebra, such a set is called a ***field***
- The definition of a vector space dose not specify the field of scalars
- By "scalars", we usually mean real numbers
- Accordingly, the vector space is called a ***real vector space***
- Scalars can also be complex numbers, in which case the vector space is called a ***complex vector space***, or prime numbers, in which case the vector space is called a ***prime vector space***, and so on...
- The field of scalars is denoted by $F$

## Vector Space Examples

### Prime Vector Space

If $p$ is prime, then the set of integers modulo $p$ is a vector space over the field of integers modulo $p$

### Not-Vector Spaces

The set of all integers is not a vector space over the field of real numbers, since the set of integers is not closed under scalar multiplication 


# Fundamental Properties of Vector Spaces

Let $V$ be a vector space over the field $F$, $u$ be a vector in $V$, and $c$ be a scalar in $F$

### Fundamental Properties of Scalar Multiplication in Vector Spaces

Let $V$ be a vector space over the field $F$, $u$ be a vector in $V$, and $c$ be a scalar in $F$

1. $0 \cdot u = 0$
   - **Explanation**: Multiplying any vector \( u \) by the scalar zero results in the zero vector.

2. $c \cdot 0 = 0$ 
   - **Explanation**: Multiplying the zero vector by any scalar \( c \) results in the zero vector.

3. $(-1) \cdot u = -u$
   - **Explanation**: Multiplying a vector \( u \) by the scalar \(-1\) results in the additive inverse (or negative) of the vector \( u \).

4. $c \cdot u = 0$ if and only if \( c = 0 \) or \( u = 0 \)
   - **Explanation**: If the product of a scalar \( c \) and a vector \( u \) is the zero vector, then either the scalar must be zero or the vector must be the zero vector.

