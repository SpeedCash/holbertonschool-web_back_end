#!/usr/bin/env python3
"""
Creates multiple asyncio.Tasks and returns their results.
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """
    Spawns multiple tasks using task_wait_random and collects their results.

    Args:
        n (int): Number of tasks to spawn.
        max_delay (int): Maximum delay for each task.

    Returns:
        List[float]: List of delays from each completed task,
        in the order they complete.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
