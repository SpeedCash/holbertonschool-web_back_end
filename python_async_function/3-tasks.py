#!/usr/bin/env python3
"""
Module to create asyncio.Tasks from a coroutine.
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task from the wait_random coroutine.

    Parameters:
    max_delay (int): The maximum delay to pass to the wait_random coroutine.

    Returns:
    asyncio.Task: A task that will execute the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
