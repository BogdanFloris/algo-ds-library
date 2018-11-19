"""
Linear time sorting algorithms as described in the CLRS
"""
import math


def counting_sort(arr: list, k, get_index=None):
    """
    Sorts the arr in O(n + k) where n = len(arr)
    :param arr: the array list to be sorted
    :param k: elements in arr are no higher then k
    :param get_index: optional lambda
    :return: a new sorted array list
    """
    counts = [0 for _ in range(k + 1)]
    sorted_arr = [None for _ in range(len(arr))]
    for elem in arr:
        if get_index is None:
            counts[elem] += 1
        else:
            counts[get_index(elem)] += 1
    for i in range(1, k + 1):
        counts[i] += counts[i - 1]
    for j in range(len(arr) - 1, -1, -1):
        if get_index is None:
            sorted_arr[counts[arr[j]] - 1] = arr[j]
            counts[arr[j]] -= 1
        else:
            sorted_arr[counts[get_index(arr[j])] - 1] = arr[j]
            counts[get_index(arr[j])] -= 1
    return sorted_arr


def radix_sort(arr: list, d):
    """
    Sorts the arr in 0(d(n+k)) where n = len(arr).
    Uses counting_sort as the stable sorting algorithm.
    :param arr: the array list to be sorted
    :param d: the number of digits in the elements of arr
    :return: new sorted array list
    """
    for i in range(d):
        arr = counting_sort(arr, k=9, get_index=lambda a: get_digit(a, i + 1))
    return arr


def get_digit(n, d):
    """
    :param n: number
    :param d: digit
    :return: d-th digit of n
    """
    for i in range(d-1):
        n //= 10
    return n % 10


def bucket_sort(arr: list):
    """
    Bucket sort algorithm
    :param arr: the array list to be sorted
    :return: new sorted array list
    """
    n = len(arr)
    buckets = [[] for _ in range(n)]
    for elem in arr:
        buckets[math.floor(n * elem)].append(elem)
    for bucket in buckets:
        bucket.sort()
    sorted_arr = []
    for bucket in buckets:
        sorted_arr += bucket
    return sorted_arr
