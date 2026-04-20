class MySegmentTree:
    def __init__(self, array):
        self.n = len(array)
        self.array = array
        self.neutral = -1
        self.segment_tree = [self.neutral for _ in range(4 * self.n)]
        self.__build(1, 0, self.n - 1)

    def __build(self, node, l, r):
        if l == r:
            self.segment_tree[node] = self.array[l]
        else:
            mid = (l + r) // 2
            self.__build(2 * node, l, mid)
            self.__build(2 * node + 1, mid + 1, r)
            self.segment_tree[node] = self.__operation(self.segment_tree[2 * node], self.segment_tree[2 * node + 1])

    def __operation(self, x, y):
        return max(x, y)

    def query(self, x, l):
        return self.__query_internal(l, x, 1, 0, self.n - 1)

    def __query_internal(self, l, x, node, node_l, node_r):
        if node_r < l or self.segment_tree[node] < x:
            return -1
        if node_l == node_r:
            return node_l

        mid = (node_l + node_r) // 2
        result = self.__query_internal(l, x, 2 * node, node_l, mid)
        if result == -1:
            result = self.__query_internal(l, x, 2 * node + 1, mid + 1, node_r)

        return result

    def update(self, idx, val):
        return self.__update_internal(1, 0, self.n - 1, idx, val)

    def __update_internal(self, node, l, r, idx, val):
        if l == r:
            self.array[idx] = val
            self.segment_tree[node] = val
        else:
            mid = (l + r) // 2
            if l <= idx <= mid:
                self.__update_internal(2 * node, l, mid, idx, val)
            else:
                self.__update_internal(2 * node + 1, mid + 1, r, idx, val)
            self.segment_tree[node] = self.__operation(self.segment_tree[2 * node], self.segment_tree[2 * node + 1])


n, m = map(int, input().split())
a = list(map(int, input().split()))
segment_tree = MySegmentTree(a)

for _ in range(m):
    q = input().split()
    if q[0] == '1':
        segment_tree.update(int(q[1]), int(q[2]))
    else:
        print(segment_tree.query(int(q[1]), int(q[2])))
