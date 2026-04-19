class MyQueue:
    def __init__(self):
        self.left = []
        self.right = []

    def enqueue(self, x):
        if len(self.left) > 0:
            self.left.append((x, max(x, self.left[-1][1])))
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
                self.right.append([item, max(self.right[-1][1], item)])
            return self.right[-1][0]

    def dequeue(self):
        if len(self.right) == 0: self.peek()
        return self.right.pop()[0]

    def max(self):
        if len(self.left) == 0:
            return self.right[-1][1]
        if len(self.right) == 0:
            return self.left[-1][1]

        return max(self.left[-1][1], self.right[-1][1])

    def len(self):
        return len(self.left) + len(self.right)


n, k = map(int, input().split())
nums = list(map(int, input().split()))
nums.append(0)

dp = [0] * (n + 1)
path = [0] * (n + 1)
prev_k = MyQueue()
prev_k.enqueue((dp[1], 1))

for i in range(2, n + 1):
    max_k, prev = prev_k.max()
    dp[i] = nums[i - 2] + max_k
    path[i] = prev
    prev_k.enqueue((dp[i], i))
    if i > k:
        prev_k.dequeue()

result_path = []
cur = n

while cur != 0:
    result_path.append(cur)
    cur = path[cur]

result_path.reverse()

print(dp[n])
print(len(result_path) - 1)
print(' '.join(map(str, result_path)))
