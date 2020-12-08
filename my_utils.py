import math
import re

def get_ints_from_string(string):
    """Method to grab all integers from a string."""
    return list(map(int, re.findall(r"-?\d+", s)))  # thanks mcpower!

def get_distance_between_points(point1, point2):
    """Calculates Euclidean distance between two points of any 
    dimension, assuming the points have the same dimension."""
    
    return math.sqrt(
        sum(
            [(point1[dim] - point2[dim]) ** 2 for dim in range(len(point1))]
        )
    )