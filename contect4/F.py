n = int(input())
intervals = []

for _ in range(n):
    l, r = map(int, input().split())
    intervals.append((l, r))

intervals.sort(key=lambda x: (x[0], x[1]))
merged_intervals = []

for interval in intervals:
    if not merged_intervals or merged_intervals[-1][1] < interval[0]:
        merged_intervals.append(interval)
    else:
        merged_intervals[-1] = (merged_intervals[-1][0], max(merged_intervals[-1][1], interval[1]))

result = sum(r - l for l, r in merged_intervals)
print(result)
