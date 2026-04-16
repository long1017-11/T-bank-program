n = int(input())
carriages = map(int, input().split())
to_add = 1
stack = []
operations = []

for c in carriages:
    stack.append(c)
    operations.append('1 1')
    while len(stack) > 0 and stack[-1] == to_add:
        stack.pop()
        operations.append('2 1')
        to_add += 1

if len(stack) > 0: print('0')
else:
    print(len(operations))
    for o in operations:
        print(o)
