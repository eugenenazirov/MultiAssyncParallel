import concurrent.futures
import threading

import requests

from multithreading.decorators import measure_time

thread_local = threading.local()



def get_session():
    if not hasattr(thread_local, 'session'):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url):
    session = get_session()
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


@measure_time
def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)


if __name__ == '__main__':
    sites = [
        "https://mitropolia.kz",
        "https://svladimir.kz"
    ] * 10

    download_all_sites(sites)
