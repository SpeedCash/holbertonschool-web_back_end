#!/usr/bin/env python3
"""
Module to work with asynchronous coroutines.
"""

import asyncio
import random
from typing import Coroutine, float

def wait_random(max_delay: int = 10) -> Coroutine[float, None, float]:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay seconds
    and returns the delay.

    Parameters:
    max_delay (int): Maximum delay time in seconds.

    Returns:
    Coroutine[float]: The delay time after which the function completes.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
