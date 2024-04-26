#!/usr/bin/env python3
"""
Defines an async coroutine that waits for a random delay and returns the delay.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay up to max_delay seconds and returns the delay.

    Args:
        max_delay (int): Maximum delay duration.

    Returns:
        float: The actual delay duration.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
