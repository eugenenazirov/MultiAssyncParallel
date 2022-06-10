import asyncio


class AsyncGenerator:

    def __init__(self, n):
        self.i = 0
        self.n = n

    def __aiter__(self):
        return self

    async def __anext__(self):
        print(f"start = {self.i}")
        await asyncio.sleep(1)
        print(f"end = {self.i}")

        if self.i >= self.n:
            raise StopAsyncIteration

        self.i += 1
        return self.i


async def main():
    async for n in AsyncGenerator(10):
        print(f"finally {n}")


if __name__ == '__main__':
    asyncio.run(main())

