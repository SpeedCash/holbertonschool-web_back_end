#!/usr/bin/env python3
"""
This module measures the runtime of four parallel async comprehensions.
"""

import asyncio
import time
from typing import List

from 1-async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel and
    measures the total runtime.
    Returns the runtime in seconds as a float.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    return end_time - start_time
