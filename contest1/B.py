def binary_search(arr, q):
    l = 0
    r = len(arr) - 1
    while r - l > 1:
        m = (l + r) // 2
        if arr[m] == q:
            return q
        elif arr[m] > q:
            r = m
        else:
            l = m

    if abs(q - arr[r]) < abs(q - arr[l]):
        return arr[r]
    return arr[l]


n, k = map(int, input().split())
arr = list(map(int, input().split()))
quarries = list(map(int, input().split()))

for q in quarries:
    print(binary_search(arr, q))
