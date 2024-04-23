#!/usr/bin/env python3
"""
Module to calculate the sum of a list of float numbers.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sums a list of floats.

    Args:
    input_list (List[float]): The list of floats to sum.

    Returns:
    float: The sum of the elements in the list.
    """
    return sum(input_list)
