def find_postfix_result(expression):
    stack = []
    for s in expression.split():
        if s == '+':
            a, b = stack.pop(), stack.pop()
            stack.append(a + b)
        elif s == '*':
            a, b = stack.pop(), stack.pop()
            stack.append(a * b)
        elif s == '-':
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        else:
            stack.append(int(s))

    return stack.pop()


expression = input().strip()
print(find_postfix_result(expression))
