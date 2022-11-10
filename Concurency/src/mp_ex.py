"""A toy example to demonstrate multiprocessing"""
import multiprocessing as mp
import itertools
import math
import time
import argparse


def do_hard_math_stuff(x, y, z):
    # Exp(Log(Cos(x)  + Cos(y) + Sin(y) - Cos(z) * Sin(z)))
    res = math.cos(x) + math.cos(y) * math.sin(y) - math.cos(z) * math.sin(z)
    res = math.log(res)
    return math.exp(res)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-j", type=int, default=1)

    x = [_ / 200 for _ in range(200)]
    # 200 * 200 * 200 = 8_000_000
    items = itertools.product(
        x,
        x,
        x,
    )
    start = time.monotonic()
    process_work(items, parser.parse_args().j)
    stop = time.monotonic()
    print(f"Calculated 8000000 in {stop-start:.2f} seconds")


def process_work(items, n=1):
    with mp.Pool(processes=n) as pool:
        res = pool.starmap(do_hard_math_stuff, items, chunksize=1000)
        pool.close()
        pool.join()
    print(list(itertools.islice(res, 10)))

if __name__ == "__main__":
    main()
