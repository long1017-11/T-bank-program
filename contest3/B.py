import sys

sys.setrecursionlimit(200000)


def is_balanced_and_bst(tree, node):
    if node == -1:
        return True, 1

    left, right = tree[node]

    if left >= node or (right <= node and right != -1):
        return False, 0

    left_is_avl, left_height = is_balanced_and_bst(tree, left)
    right_is_avl, right_height = is_balanced_and_bst(tree, right)

    if not left_is_avl or not right_is_avl:
        return False, 0

    if abs(left_height - right_height) > 1:
        return False, 0

    height = max(left_height, right_height) + 1
    return True, height


n, r = map(int, input().split())
tree = []

for i in range(n):
    li, ri = map(int, input().split())
    tree.append((li, ri))

balanced, _ = is_balanced_and_bst(tree, r)

if balanced:
    print(1)
else:
    print(0)
