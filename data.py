from pathlib import Path
import numpy as np

cities = []
CITIES_PATH = Path("data/cities.csv")
with CITIES_PATH.open() as f:
    f.readline()
    for line in f.readlines():
        _, x, y = line.split(",")
        cities.append((x, y))

cities = np.array(cities, dtype=np.float16)


def primes(limit):
    primes = {}
    for i in range(2, limit + 1):
        primes[i] = True
    for i in primes:
        factors = range(i, limit + 1, i)
        for f in factors[1:]:
            primes[f] = False

    return set((i for i in primes if primes[i]))


prime_set = primes(len(cities))
prime_cities = np.array(list(prime_set))
