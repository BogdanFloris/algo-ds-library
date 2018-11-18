"""
Quicksort algorithm
"""


def quick_sort(arr):
    """
    Sorts the array list in place.
    Uses the helper functions quick_sort_helper and partition.
    :param arr: the array list to be sorted
    """
    quick_sort_helper(arr, 0, len(arr) - 1)


def quick_sort_helper(arr, first, last):
    if first < last:
        pivot = partition(arr, first, last)
        quick_sort_helper(arr, first, pivot - 1)
        quick_sort_helper(arr, pivot + 1, last)


def partition(arr, first, last):
    pivot = arr[last]
    i = first - 1
    for j in range(first, last):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[last] = arr[last], arr[i + 1]
    return i + 1
