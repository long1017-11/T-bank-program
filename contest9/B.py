import sys


class MySegmentTree:
    def __init__(self, array):
        self.n = len(array)
        self.array = array
        self.neutral = [10 ** 9 + 1, 0]
        self.segment_tree = [self.neutral for _ in range(4 * self.n)]
        self.__build(1, 0, self.n - 1)

    def __build(self, node, l, r):
        if l == r:
            self.segment_tree[node] = [self.array[l], 1]
        else:
            mid = (l + r) // 2
            self.__build(2 * node, l, mid)
            self.__build(2 * node + 1, mid + 1, r)
            self.segment_tree[node] = self.__operation(self.segment_tree[2 * node], self.segment_tree[2 * node + 1])

    def __operation(self, x, y):
        if x[0] < y[0]:
            return x
        if x[0] > y[0]:
            return y
        return [x[0], x[1] + y[1]]

    def query(self, l, r):
        return self.__query_internal(1, 0, self.n - 1, l, r)

    def update(self, idx, val):
        return self.__update_internal(1, 0, self.n - 1, idx, val)

    def __update_internal(self, node, l, r, idx, val):
        if l == r:
            self.array[idx] = val
            self.segment_tree[node] = [val, 1]
        else:
            mid = (l + r) // 2
            if l <= idx <= mid:
                self.__update_internal(2 * node, l, mid, idx, val)
            else:
                self.__update_internal(2 * node + 1, mid + 1, r, idx, val)
            self.segment_tree[node] = self.__operation(self.segment_tree[2 * node], self.segment_tree[2 * node + 1])

    def __query_internal(self, node, tl, tr, l, r):
        if r < tl or tr < l:
            return self.neutral
        if l <= tl and tr <= r:
            return self.segment_tree[node]
        tm = (tl + tr) // 2
        return self.__operation(self.__query_internal(2 * node, tl, tm, l, r),
                                self.__query_internal(2 * node + 1, tm + 1, tr, l, r))


file = sys.stdin.readlines()
n, m = map(int, file[0].rstrip('\n').split())
array = list(map(int, file[1].rstrip('\n').split()))
segment_tree = MySegmentTree(array)

for i in range(2, m + 2):
    q = file[i].rstrip('\n').split()
    if q[0] == '1':
        segment_tree.update(int(q[1]), int(q[2]))
    else:
        ans = segment_tree.query(int(q[1]), int(q[2]) - 1)
        print(f'{ans[0]} {ans[1]}')
