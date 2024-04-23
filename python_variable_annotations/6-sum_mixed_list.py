#!/usr/bin/env python3
"""
Module to calculate the sum of a list of mixed integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums a list of integers and floats.

    Args:
    mxd_lst (List[Union[int, float]]): The list containing integers and floats.

    Returns:
    float: The sum of the elements in the list.
    """
    return float(sum(mxd_lst))
