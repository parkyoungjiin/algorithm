import sys
input = sys.stdin.readline

n = int(input())

tree = {}
for _ in range(n):
    val, left, right = input().split()
    tree[val] = [left,right]

# 전위(루 -> 왼 -> 오)
def pre_order(v):
    if v != '.':
        print(v, end='')
        #왼
        pre_order(tree.get(v)[0])
        #오
        pre_order(tree.get(v)[1])

# 중위 (왼 -> 루 -> 오)
def in_order(v):
    if v != '.':
        # 왼
        in_order(tree.get(v)[0])
        # 루트
        print(v, end='')
        # 오른
        in_order(tree.get(v)[1])

# 후위 (왼 -> 오 -> 루)
def post_order(v):
    if v != '.':
        post_order(tree.get(v)[0])
        post_order(tree.get(v)[1])
        print(v, end ='')

# 재귀?

pre_order('A')
print('')
in_order('A')
print('')
post_order('A')


