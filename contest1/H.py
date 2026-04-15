n = int(input())
str = input().strip()

freq_map = {}
for c in str:
    if c in freq_map:
        freq_map[c] += 1
    else:
        freq_map[c] = 1

start, end, mid = '', '', ''

for c in sorted(freq_map):
    while freq_map[c] >= 2:
        freq_map[c] -= 2
        start = start + c
        end = c + end
    if mid == '' and freq_map[c] == 1:
        mid = c

print(f'{start}{mid}{end}')
