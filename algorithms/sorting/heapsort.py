"""
Heap Sort algorithm
"""
from datastructures.heap import MaxHeap


def heap_sort(a: list):
    """
    Sorts a list in O(n * log(n)) time, where n is the length of a.
    :param a: the list to be sorted
    :return:
    """
    heap = MaxHeap(a)
    for i in range(heap.current_size, 1, -1):
        heap.heap_list[1], heap.heap_list[i] = heap.heap_list[i], heap.heap_list[1]
        heap.current_size -= 1
        heap.heapify(1)
    return heap.get_array()
