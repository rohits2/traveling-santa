from data import cities, prime_set
import numpy as np
import numpy.linalg as la


def metric(path):
    visited_cities = cities[path, :]
    distances = la.norm(visited_cities[1:] - visited_cities[:-1], axis=1)
    for i in range(9, len(path)-1, 10):
        if path[i] not in prime_set:
            distances[i] *= 1.1
    return distances.sum()
