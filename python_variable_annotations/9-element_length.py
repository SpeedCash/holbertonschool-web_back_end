#!/usr/bin/env python3
"""
Module to calculate the length of elements in an iterable.
"""

from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable containing sequences, and returns a list of tuples.
    Each tuple contains a sequence and its length.

    Args:
    lst (Iterable[Sequence]): The iterable of sequences.

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples, each containing\
        a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
