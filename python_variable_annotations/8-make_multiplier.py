#!/usr/bin/env python3
"""
Module to create a multiplier function based on a given float multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function that multiplies its input by a predefined multiplier.

    Args:
    multiplier (float): The number that will be used as the multiplier.

    Returns:
    Callable[[float], float]: A function that takes a float and returns\
        it multiplied by the multiplier.
    """
    def multiplier_func(value: float) -> float:
        return value * multiplier
    return multiplier_func
