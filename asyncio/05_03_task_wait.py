# this code doesn't work correctly, there are an exception with dunder __aenter__


import asyncio, aiohttp
from asyncio import FIRST_COMPLETED
from collections import namedtuple


Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

services = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query')
)


async def get_json(url):
    async with aiohttp.ClientSession as session:
        async with session.get(url) as response:
            return await response.json()


async def fetch_ip(service):
    print(f"Fetching IP from {service.name}")

    json_response = await get_json(service.url)
    ip = json_response[service.ip_attr]
    return f"{service.name} finished with result {ip}"


async def main():
    coros = [fetch_ip(service) for service in services]
    coro1 = coros[0]
    coro2 = coros[1]
    await asyncio.gather(coro1, coro2)

    for x in done:
        print(x.result())


if __name__ == '__main__':
    asyncio.run(main())
