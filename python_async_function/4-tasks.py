#!/usr/bin/env python3
"""
Module to execute multiple tasks concurrently and gather the results.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random() n times with the specified max_delay
    and returns a list of the delays.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    completed = []
    for future in asyncio.as_completed(tasks):
        result = await future
        completed.append(result)
    return completed
