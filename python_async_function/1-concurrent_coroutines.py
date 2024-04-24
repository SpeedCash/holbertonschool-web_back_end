#!/usr/bin/env python3
"""
Module to execute multiple coroutines concurrently and gather the results.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random() n times with the specified max_delay and
    returns a list of the delays.

    Parameters:
    n (int): The number of times to spawn the wait_random coroutine.
    max_delay (int): The maximum delay to be passed to wait_random.

    Returns:
    List[float]: A list of float values representing
    the delays, in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    completed = []
    for future in asyncio.as_completed(tasks):
        result = await future
        completed.append(result)
    return completed
