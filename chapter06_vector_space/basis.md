

# Definition

> A basis is a set of vectors that have two key properties:
>
> **Linear independence**: No vector in the basis can be built by combining the other vectors in the basis. It's like saying you can't build a specific LEGO brick by putting together other bricks in your chosen set.
>
> **Spanning**: You can build any vector in your space by combining the vectors in the basis. This is like saying you can build any LEGO structure using only the bricks in your chosen set.
>

# Example: The coordinate plane

In the regular 2D coordinate plane, the standard basis vectors are:

i-hat (î): The vector pointing one unit to the right (1, 0)
j-hat (ĵ): The vector pointing one unit upwards (0, 1)
These two vectors are linearly independent (you can't make one by adding multiples of the other) and they span the entire plane (you can reach any point by moving some amount horizontally and some amount vertically).

# Why is a basis important?

- *Coordinates*: A basis gives you a way to describe any vector in your space using numbers. These numbers are like coordinates, telling you how much of each basis vector you need to combine to get your desired vector.
- *Dimension*: The number of vectors in a basis tells you the dimension of your space. For example, the coordinate plane has two basis vectors, so it's two-dimensional.
- *Change of basis*: You can choose different basis vectors to describe the same space. It's like switching to a different set of LEGO bricks – you can still build everything, but you might use different combinations.
Key takeaways


# Theorem - Cardinality of Bases

- If two bases exist for a vector space, then they must have the same number of vectors
  - This is because if one basis has more vectors than the other, then the basis with more vectors would be linearly dependent, which is a contradiction
  - Similarly, if one basis has fewer vectors than the other, then the basis with fewer vectors would not span the vector space, which is also a contradiction
  - Therefore, two bases for a vector space must have the same number of vectors
  - I.e., the cardinality of any two bases for a vector space is the same

# Theorem - Basis of a Vector Space

> If a vector space $V$ has a basis with $n$ vectors, then any set of vectors in $V$ that contains more than $n$ vectors is linearly dependent.


# Theorem - Smallest Size

> The basis of a vector space is the smallest set of vectors that spans the vector space and is linearly independent.
>
> If a vector space $V$ has a basis with $n$ vectors, then any set of vectors in $V$ that contains fewer than $n$ vectors does not span the vector space, and any set of vectors in $V$ that contains more than $n$ vectors is linearly dependent.


# The Graham Schmidt (or Marquis de Laplace) Process to Find an Orthonormal Basis

> Gram-Schmidt process: This is a specific algorithm in linear algebra used to orthonormalize a set of vectors. It systematically modifies the original vectors to make them orthogonal to each other while maintaining the same span.


1. Start with a set of linearly independent vectors.
2. project the first vector onto the second vector and subtract it from the second vector.

   $w_2 = v_2 - \frac{v_2 \cdot w_1}{w_1 \cdot w_1}w_1$ 

   project w onto u, then do w - result

## Two Steps

1. Normalize the first vector to get the first basis vector.
2. For each subsequent vector, subtract the projection of the vector onto the previous basis vectors to get the next basis vector.
3. Repeat until you have an orthonormal basis.


![alt text](pictures/graham-schmidt-2steps.png)

![alt text](../../references/graham-schmidt-process.gif)


# Theorem - Culling Method

- If you have a set of vectors that spans a vector space, you can cull it down to a basis by removing any vectors that are linearly dependent on the others
  - I.e., if you have a set of vectors that spans a vector space, you can remove any vectors that are linearly dependent on the others to get a basis
  - This is because the basis is the smallest set of vectors that spans the vector space and is linearly independent
  - Therefore, any vectors that are linearly dependent on the others are not necessary to span the vector space, and can be removed to get a basis

![alt text](pictures/culling-method.png)