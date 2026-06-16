#!/usr/bin/env python3
"""Async generator module"""

import asyncio
import random


async def async_generator():
    """Async generator that yields 10 random numbers with 1 second delay between each."""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
