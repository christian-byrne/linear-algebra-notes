from chapter05_orthogonality.graham_schmidt_orthogonality import GrahamSchmidt
from chapter01_vector.vector_class import Vector

from typing import List

class LinearDependenceTest:
    def __init__(self, vectors):
        self.vectors = vectors
        self.size = len(vectors)

    def zero_vector_test(self):
        """
        Test if the set is linearly dependent by doing orthogonalization on every
        vector pair in the set and seeing if any of the resulting vectors is the zero vector.

        The zero vector indicates that the set is linearly dependent.
        """
        permuations = self.__get_vector_pair_permutations()
        for pair in permuations:
            gs = GrahamSchmidt(pair)
            orthogonalized: List[Vector] = gs.orthogonalize().orthogonal_vectors
            if any([v.is_zero_vector() for v in orthogonalized]):
                return True, "Linearly dependent set"
        return False, "Linearly independent set"

    def __get_vector_pair_permutations(self):
        permutations = self.__permutations(self.size, 2)
        print(f"Found {len(permutations)} permutations")
        return permutations

    def __permutations(self, n, k):
        if k == 1:
            return [[self.vectors[n - 1]] for i in range(n)]
        else:
            perms = []
            for i in range(n):
                perms += [
                    [self.vectors[i]] + perm for perm in self.__permutations(n, k - 1)
                ]
            return perms
