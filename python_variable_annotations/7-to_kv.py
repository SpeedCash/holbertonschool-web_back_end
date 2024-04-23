#!/usr/bin/env python3
"""
Module to create a tuple from a string and the square of a number.
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple containing a string and the square of a number.

    Args:
    k (str): The string to be included in the tuple.
    v (Union[int, float]): The number whose square will be calculated\
        and included in the tuple.

    Returns:
    Tuple[str, float]: A tuple where the first element is the string\
        and the second element is the square of the number as a float.
    """
    return (k, float(v ** 2))
