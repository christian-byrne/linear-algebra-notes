from chapter01_vector.vector_class import Vector
from chapter01_vector.parametric_vector import ParametricVector

from typing import Union, List, Tuple, Any


class LinearCombination:
    """Class to represent a linear combination of vectors.
    It stores a list of ParametricVector objects whose coefficients can
    be changed. 
        
		The current evaluated value of the linear combination can
    be accessed without having to alter the class's state.
    
    Args:
				terms (List[ParametricVector]): List of ParametricVector objects.

    """

    def __init__(self, terms: List[ParametricVector]):
        self.terms = terms

    def __call__(self) -> Vector:
        return sum([term() for term in self.terms])
