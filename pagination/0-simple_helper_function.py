#!/usr/bin/env python3
"""
A simple helper function for pagination.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.

    Parameters:
    - page (int): The page number (1-indexed).
    - page_size (int): The size of each page.

    Returns:
    - Tuple[int, int]: A tuple of the start and end index.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return start, end
