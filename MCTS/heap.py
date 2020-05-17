import random as rd


class Heap:
    def __init__(self, arr=None):
        if arr is None:
            self.heap = []
            self.len = 0
        else:
            self.heap = arr[:]
            self.len = len(self.heap)
            self.heapify()

    def __len__(self):
        return self.len

    def __getitem__(self, idx):
        return self.heap[idx]

    def __str__(self):
        return str(self.heap)

    def _sift(self, idx):
        left = idx * 2 + 1
        right = idx * 2 + 2
        target = idx

        if left < self.len:
            if not self.compare(self.heap[target], self.heap[left]):
                target = left

        if right < self.len:
            if not self.compare(self.heap[target], self.heap[right]):
                target = right

        if target != idx:
            self.swap(target, idx)
            self._sift(target)

    def push(self, value):
        self.heap.append(value)
        self.set_to(value, self.len)
        self.len += 1
        idx = self.len - 1
        while idx:
            idx = (idx - 1) // 2
            self._sift(idx)

    def pop(self):
        if self.len == 0:
            raise IndexError('pop from an empty heap')
        if self.len == 1:
            self.len -= 1
            return self.heap.pop()
        self.swap(0, self.len - 1)
        value = self.heap.pop()
        self.len -= 1
        self._sift(0)
        return value

    def update(self, idx):
        parent = (idx - 1) // 2
        if idx != 0:
            if not self.compare(self.heap[parent], self.heap[idx]):
                while idx:
                    idx = (idx - 1) // 2
                    self._sift(idx)
                return
        self._sift(idx)

    def delete(self, idx):
        if self.len == 0:
            raise IndexError('delete from an empty heap')
        self.swap(idx, self.len - 1)
        self.heap.pop()
        self.len -= 1
        self.update(idx)

    def top(self):
        return self.heap[0]

    def heapify(self):
        for idx in range(self.len // 2, -1, -1):
            self._sift(idx)

    def swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]
        self.set_to(self.heap[idx1], idx2)
        self.set_to(self.heap[idx2], idx1)

    def set_to(self, value, idx):
        pass

    @staticmethod
    def compare(v1, v2) -> bool:
        """
        :param v1: value to be upper
        :param v2: value to be lower
        :return: return true if order is valid else false
        """
        return v1 < v2

    def valid(self):
        if self.len != len(self.heap):
            print('len invalid', self.len, len(self.heap))
            return False
        for i in range(self.len // 2):
            if i * 2 + 1 < self.len:
                if not self.compare(self.heap[i], self.heap[i * 2 + 1]):
                    return False
            if i * 2 + 2 < self.len:
                if not self.compare(self.heap[i], self.heap[i * 2 + 2]):
                    return False
        return True


