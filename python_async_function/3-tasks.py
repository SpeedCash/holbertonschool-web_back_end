#!/usr/bin/env python3
"""
Creates an asyncio.Task to run an async function with a delay.
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """
    Takes an integer max_delay and returns an asyncio.Task running wait_random.

    Args:
        max_delay (int): Maximum delay time for the async function.

    Returns:
        asyncio.Task: The created task.
    """
    return asyncio.create_task(wait_random(max_delay))
