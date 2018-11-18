"""
Binary Heap Implementation
"""
from abc import ABC, abstractmethod
import sys


class Heap(ABC):
    """
    A heap is represented by a list of elements and the current size.
    Notice that an empty heap contains the element 0 already.
    This helps with calculating indices.
    """
    def __init__(self, initial=None):
        if initial is None:
            # build empty heap
            self.heap_list = [0]
            self.current_size = 0
        else:
            # build heap from list
            self.heap_list = [0] + initial
            self.current_size = len(initial)
            self.build_heap()

    def build_heap(self):
        """
        Builds heap from a random list
        """
        for i in range(self.current_size//2, 0, -1):
            self.heapify(i)

    @abstractmethod
    def heapify(self, i):
        """
        Maintains the Heap property (Max or Min).
        :param i: the subtrees rooted at left(i) and right(i) are heaps.
        """
        pass

    @abstractmethod
    def insert(self, key):
        """
        Inserts an element into the heap
        :param key: key to be inserted
        """
        pass

    def get_array(self):
        """
        :return: the array
        """
        return self.heap_list[1:]

    @staticmethod
    def parent(i):
        """
        Returns the index of the parent of i.
        :param i: index of the current element
        :return: the index of the parent of i
        """
        return i//2

    @staticmethod
    def left(i):
        """
        Returns the index of the left child of i.
        :param i: the index of the current element
        :return: the index of the left child of i
        """
        return 2 * i

    @staticmethod
    def right(i):
        """
        Returns the index of the right child of i.
        :param i: the index of the current element
        :return: the index of the right child of i
        """
        return 2 * i + 1


class MaxHeap(Heap):
    def max(self):
        """
        :return: the maximum element
        """
        if self.current_size is 0:
            raise ValueError("No elements in the Heap.")
        return self.heap_list[1]

    def extract_max(self):
        """
        Removes the maximum element and returns it.
        :return: the maximum element
        """
        if self.current_size is 0:
            raise ValueError("No elements in the Heap")
        maximum = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heapify(1)
        return maximum

    def increase_key(self, i, key):
        """
        Increases the key at index i
        :param i: index to be changed
        :param key: new key
        """
        if key < self.heap_list[i]:
            raise ValueError("New key is smaller than current key.")
        self.heap_list[i] = key
        while i > 1 and self.heap_list[self.parent(i)] < self.heap_list[i]:
            self.heap_list[i], self.heap_list[self.parent(i)] =\
                self.heap_list[self.parent(i)], self.heap_list[i]
            i = self.parent(i)

    def insert(self, key):
        self.current_size += 1
        self.heap_list[self.current_size] = -sys.maxsize
        self.increase_key(self.current_size, key)

    def heapify(self, i):
        """
        Maintains the Max Heap property.
        :param i: the subtrees rooted at left(i) and right(i) are max heaps.
        """
        left = self.left(i)
        right = self.right(i)
        if left <= self.current_size and self.heap_list[left] > self.heap_list[i]:
            largest = left
        else:
            largest = i
        if right <= self.current_size and self.heap_list[right] > self.heap_list[largest]:
            largest = right
        if largest != i:
            self.heap_list[i], self.heap_list[largest] = self.heap_list[largest], self.heap_list[i]
            self.heapify(largest)


class MinHeap(Heap):
    def heapify(self, i):
        """
        Maintains the Min Heap property
        :param i: the subtress rooted at left(i) and right(i) are min heaps.
        """
        pass

    def insert(self, key):
        pass
