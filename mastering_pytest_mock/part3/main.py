import asyncio
from random import randint


async def long_computation() -> str:
    random_number = randint(1,10)
    await asyncio.sleep(random_number)
    return "DONE"

