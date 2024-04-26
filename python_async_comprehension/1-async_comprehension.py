#!/usr/bin/env python3
"""
This module uses an async comprehension to collect random numbers
from an asynchronous generator.
"""

import asyncio
from typing import List

from 0-async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehension
    over async_generator.
    Returns a list of these random numbers.
    """
    return [i async for i in async_generator()]
