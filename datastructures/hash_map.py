"""
Hash Map Python implementation
"""


class HashMap:
    def __init__(self):
        # initial number of elements in the map
        self._size = 0
        # 10 initial slots
        self._num_buckets = 10
        # create list of Nones
        self._bucket_list: list = [None] * self._num_buckets

    def size(self):
        """
        :return: number of elements in the map
        """
        return self._size

    def get(self, key):
        """
        Returns the value given a key.
        :param key: key
        :return: value
        """
        index = self._get_index(key)
        head = self._bucket_list[index]
        if head is None:
            raise ValueError("Key not in the map.")
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next

    def put(self, key, value):
        """
        Puts the key, value pair in the map
        :param key: key
        :param value: value
        """
        index = self._get_index(key)
        head = self._bucket_list[index]
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next
        self._size += 1
        head = self._bucket_list[index]
        new_node = Node(key, value)
        new_node.next = head
        self._bucket_list[index] = new_node
        if self._should_expand():
            self.expand()

    def _get_index(self, key):
        """
        :param key: key
        :return: the index for the list of the key
        """
        return hash(key) % self._num_buckets

    def _should_expand(self):
        """
        Checks if the map should expand. The threshold is 0.7
        """
        return self.size() / self._num_buckets >= 0.7

    def expand(self):
        """
        Doubles the size of map and copies the elements.
        """
        pass


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next: Node = None
