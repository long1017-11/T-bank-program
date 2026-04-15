def count_cycles(nums, cnt):
    global r
    cnt -= len(nums) - r - 1
    if cnt == len(nums) or cnt == 0:
        return 1

    while nums[r] == 1 and cnt > 0:
        r -= 1
        cnt -= 1

    return cnt + 1


n = int(input())
changes = list(map(int, input().split()))

print(1, end=' ')
array = [0] * n
ones_cnt = 0
r = n - 1

for c in changes:
    array[c - 1] = 1
    ones_cnt += 1
    print(count_cycles(array, ones_cnt), end=' ')
