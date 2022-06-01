import asyncio
from multithreading.decorators import async_measure_time


async def tick():
    print("tick")
    await asyncio.sleep(1)
    print("tock")


@async_measure_time
async def main():
    # for _ in range(3):
    #     tick()
    await asyncio.gather(tick(), tick(), tick())


if __name__ == '__main__':
    asyncio.run(main())

