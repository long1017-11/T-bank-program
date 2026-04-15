from sys import stdout


def query(x):
    print(x)
    stdout.flush()
    return input()


def guess_number(n):
    l = 1
    r = n
    while r - l > 1:
        m = (l + r) // 2
        response = query(m)
        if response == '<':
            r = m - 1
        else:
            l = m

    if r == l or query(r) == '>=':
        print(f'! {r}')
    else:
        print(f'! {l}')


n = int(input())
guess_number(n)
