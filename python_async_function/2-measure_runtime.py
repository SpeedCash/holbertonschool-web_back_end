#!/usr/bin/env python3
"""
Measures the average execution time per call of an asynchronous routine.
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n called with n and max_delay,
    and returns the average time per call.

    Args:
        n (int): The number of async tasks to run.
        max_delay (int): The maximum delay for each task.

    Returns:
        float: The average execution time per task.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
