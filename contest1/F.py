def merge(array, start, mid, end):
    global inversion_counter
    l = start
    r = mid + 1
    temp_i = start
    while l <= mid or r <= end:
        if r > end or (l <= mid and array[l] <= array[r]):
            temp_array[temp_i] = array[l]
            l += 1
        else:
            temp_array[temp_i] = array[r]
            inversion_counter += mid + 1 - l
            r += 1
        temp_i += 1

    for i in range(start, end + 1):
        array[i] = temp_array[i]


def merge_sort(array, start, end):
    if start == end: return
    mid = (start + end) // 2
    merge_sort(array, start, mid)
    merge_sort(array, mid + 1, end)
    merge(array, start, mid, end)


n = int(input())
array = list(map(int, input().split()))

temp_array = [0] * n
inversion_counter = 0
merge_sort(array, 0, n - 1)

print(inversion_counter)
print(' '.join(map(str, array)))
