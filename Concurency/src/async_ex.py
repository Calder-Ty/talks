"""An example of writing asynchronous code"""
import argparse
import asyncio
import time


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sync", action="store_true")
    args = parser.parse_args()

    users = ["Nathan", "Austin", "Tyler", "Brandon", "Derek", "Dallin"]
    start = time.monotonic()
    if args.sync:
        total = fetch_data_from_api(users)
        stop = time.monotonic()
    else:
        # Async code Has to be called inside other Async functions, or started by
        # and Event Loop
        # loop = asyncio.get_event_loop()
        total = asyncio.run(async_fetch_data_from_api(users))
        # total = loop.run_until_complete(async_fetch_data_from_api(users))
        stop = time.monotonic()
        tot = stop - start
    print("Ran {} calls in {} seconds".format(total, tot))


def fetch_data_from_api(users) -> int:
    res = []
    for user in users:
        res.append(sync_call_api(user))
    return sum(res)


async def async_fetch_data_from_api(users):
    res = await asyncio.gather(*[async_call_api(user) for user in users])
    return sum(res)


def sync_call_api(user):
    time.sleep(1)
    return 1


async def async_call_api(user):
    await asyncio.sleep(1)
    return 1


if __name__ == "__main__":
    main()
