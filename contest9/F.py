class MySegmentTree:
    def __init__(self, array):
        self.n = len(array)
        self.array = array
        self.neutral = 0
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
        return x + y

    def query(self, l, r):
        return self.__query_internal(1, 0, self.n - 1, l, r)

    def update(self, idx, val):
        return self.__update_internal(1, 0, self.n - 1, idx, val)

    def __update_internal(self, node, l, r, idx, val):
        if l == r:
            self.array[idx] += val
            self.segment_tree[node] += val
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


n = int(input())
a = list(map(int, input().split()))

compress = {value: idx for idx, value in enumerate(sorted(set(a)))}
st_2 = MySegmentTree([0] * (n + 1))
st_3 = MySegmentTree([0] * (n + 1))
cnt = 0

for e in a:
    i = compress[e]
    st_2.update(i, 1)
    st_3.update(i, st_2.query(i + 1, n))
    cnt += st_3.query(i + 1, n)

print(cnt)
