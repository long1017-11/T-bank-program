class MyHeap:
    def __init__(self):
        self.heap = []

    def _lower(self, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._lower(largest)

    def _raise(self, i):
        parent = (i - 1) // 2

        if i > 0 and self.heap[i] > self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            self._raise(parent)

    def insert(self, item):
        self.heap.append(item)
        self._raise(len(self.heap) - 1)

    def extract(self):
        if len(self.heap) == 0:
            return None

        item = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._lower(0)

        return item


n = int(input())
heap = MyHeap()

for _ in range(n):
    t = input().split()
    if t[0] == '0':
        heap.insert(int(t[1]))
    else:
        print(heap.extract())
