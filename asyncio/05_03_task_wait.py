import socket
import asyncio
import aiohttp
from collections import namedtuple


Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

services = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query')
)


async def get_json(url):
    conn = aiohttp.TCPConnector(family=socket.AF_INET, ssl=True, )
    async with aiohttp.ClientSession(connector=conn) as session:
        async with session.get(url) as response:
            return await response.json()


async def fetch_ip(service):
    print(f"Fetching IP from {service.name}")

    json_response = await get_json(service.url)
    ip = json_response[service.ip_attr]
    return f"{service.name} finished with result {ip}"


async def main():
    tasks = set()
    for service in services:
        task = asyncio.create_task(fetch_ip(service))
        tasks.add(task)

    pending, done = await asyncio.wait(tasks)

    for x in done:
        print(x.result())


if __name__ == '__main__':
    asyncio.run(main())
