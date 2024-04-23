#!/usr/bin/env python3
"""
Module to calculate the floor of a float number.
"""

from math import floor as math_floor


def floor(n: float) -> int:
    """
    Calculates the floor of a float.

    Args:
    n (float): The float number to calculate the floor of.

    Returns:
    int: The floor of the float number.
    """
    return math_floor(n)
