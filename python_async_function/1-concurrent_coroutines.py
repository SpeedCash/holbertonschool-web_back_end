#!/usr/bin/env python3
"""
Spawns multiple async tasks and returns the delays in ascending order.
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.
    Returns a list of the delays in ascending order.

    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        List[float]: Delays from each wait_random call,
        sorted naturally by completion order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
