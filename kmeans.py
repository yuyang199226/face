from collections import defaultdict
from random import uniform
from math import sqrt
from vis import display
import numpy as np
import random


def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    NB. points can have more dimensions than 2

    Returns a new point which is the center of all the points.
    """
    dimensions = len(points[0])

    new_center = []

    for dimension in range(dimensions):
        dim_sum = 0  # dimension sum
        for p in points:
            dim_sum += p[dimension]

        # average of each dimension
        new_center.append(dim_sum / float(len(points)))

    return new_center


def update_centers(data_set, clusters):
    """
    Accepts a dataset and a list of assignments; the indexes
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers where `k` is the number of unique assignments.
    """
    centers = []
    for c_id, points in clusters.items():
        centers.append(list(np.asarray(points).mean(axis=0)))

    return centers

def assign_points2(data_points, centers):
    clusters = defaultdict(list)
    for point in data_points:
        shortest = float('inf')
        index = -1
        for i in range(len(centers)):
            dist = distance(centers[i], point)
            if dist < shortest:
                shortest = dist
                index = i
        clusters[index].append(point)
    return clusters




def distance(a, b):
    s = sum(np.square(np.asarray(a) - np.asarray(b)))
    return s

def init_u(data_set, k):
    centers = random.sample(data_set, k)
    return centers


def generate_k(data_set, k):
    """
    Given `data_set`, which is an array of arrays,
    find the minimum and maximum for each coordinate, a range.
    Generate `k` random points between the ranges.
    Return an array of the random points within the ranges.
    """
    centers = []
    dimensions = len(data_set[0])
    min_max = defaultdict(int)

    for point in data_set:
        for i in range(dimensions):
            val = point[i]
            min_key = 'min_%d' % i
            max_key = 'max_%d' % i
            if min_key not in min_max or val < min_max[min_key]:
                min_max[min_key] = val
            if max_key not in min_max or val > min_max[max_key]:
                min_max[max_key] = val

    for _k in range(k):
        rand_point = []
        for i in range(dimensions):
            min_val = min_max['min_%d' % i]
            max_val = min_max['max_%d' % i]

            rand_point.append(uniform(min_val, max_val))

        centers.append(rand_point)

    return centers


def k_means(dataset, k):
    new_centers = init_u(dataset, k)
    #print(k_points)
    clusters = assign_points2(dataset, new_centers)
    old_centers = None
    count = 0
    while old_centers != new_centers:
        old_centers = new_centers
        new_centers = update_centers(dataset, clusters)
        clusters = assign_points2(dataset, new_centers)
        print(clusters)
        count += 1
    print(count)
    return clusters

points = [
     [1, 2],
     [1, 1],
     [2, 3],
     [1, 2],
     [2, 1],
     [3, 1],
     [5, 4],
     [5, 5],
     [6, 5],
     [10, 12],
     [10, 15],
     [11, 11],
     [11, 12],
     [11, 8],
     [11, 13],
     [14, 18],
     [14, 14],
     [2, 2],
     [2, 6],
     [1, 3],
     [13, 7],
     [13, 9],
     ]
res = k_means(points, 3)
display(res)
