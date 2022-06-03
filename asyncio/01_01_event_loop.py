import asyncio
from multithreading.decorators import async_measure_time


async def tick():
    print("tick")
    await asyncio.sleep(1)
    print("tock")

    loop = asyncio.get_running_loop()
    if loop.is_running():
        print("the loop is still running")


async def main():
    awaitable = asyncio.gather(tick(), tick(), tick())

    for task in asyncio.all_tasks():
        print(task, end='\n')

    await awaitable

if __name__ == '__main__':

    # asyncio.run(main())
    # coroutine = main()
    # print(coroutine)

    loop = asyncio.get_event_loop()
    try:
        loop.create_task(main())
        loop.run_forever()
        # loop.run_until_complete(main())
        print("coroutines have finished")
    except KeyboardInterrupt:
        print("manually closed app")
    finally:
        loop.close()
        print(loop.is_closed())

