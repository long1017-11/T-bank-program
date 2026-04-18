n, c = map(int, input().split())
intervals = []

for num in range(1, n + 1):
    start, time = map(int, input().split())
    intervals.append((start, start + time, num))

intervals.sort(key=lambda x: x[1])
cur_time = 0
chosen_numbers = []

for start, end, num in intervals:
    if cur_time <= start:
        cur_time = end
        chosen_numbers.append(num)

cnt = len(chosen_numbers)
print(cnt * c)
print(cnt)
print(' '.join(map(str, chosen_numbers)))
