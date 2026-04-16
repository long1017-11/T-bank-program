class MyQueue:
    def __init__(self):
        self.left = []
        self.right = []

    def enqueue(self, x):
        if len(self.left) > 0:
            self.left.append((x, min(x, self.left[-1][1])))
        else:
            self.left.append((x, x))

    def peek(self):
        if len(self.right) > 0:
            return self.right[-1][0]
        else:
            item = self.left.pop()[0]
            self.right.append((item, item))
            while len(self.left) > 0:
                item = self.left.pop()[0]
                self.right.append([item, min(self.right[-1][1], item)])
            return self.right[-1][0]

    def dequeue(self):
        if len(self.right) == 0: self.peek()
        return self.right.pop()[0]

    def min(self):
        if len(self.left) == 0:
            return self.right[-1][1]
        if len(self.right) == 0:
            return self.left[-1][1]

        return min(self.left[-1][1], self.right[-1][1])

    def len(self):
        return len(self.left) + len(self.right)


n, k = map(int, input().split())
seq = list(map(int, input().split()))
queue = MyQueue()

for num in seq:
    queue.enqueue(num)
    if queue.len() > k:
        queue.dequeue()
    if queue.len() == k:
        print(queue.min(), end=' ')
