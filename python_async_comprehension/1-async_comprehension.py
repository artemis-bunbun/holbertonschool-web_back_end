#!/usr/bin/env python3
"""Async comprehension module"""

from importlib import import_module

async_generator = import_module('0-async_generator').async_generator


async def async_comprehension():
    """Collect 10 random numbers using async comprehension."""
    return [x async for x in async_generator()]
