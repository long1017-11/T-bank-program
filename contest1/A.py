def binary_search(arr, q):
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == q:
            return True
        elif arr[m] > q:
            r = m - 1
        else:
            l = m + 1

    return False


n, k = map(int, input().split())
arr = list(map(int, input().split()))
quarries = list(map(int, input().split()))

for q in quarries:
    if binary_search(arr, q): print('YES')
    else: print('NO')
