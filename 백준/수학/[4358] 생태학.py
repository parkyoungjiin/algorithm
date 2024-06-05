import sys

input = sys.stdin.readline

dic = dict()
while 1:
    tree = input().rstrip() 
    if not tree:
        break

    if not dic.get(tree):
        dic[tree] = 1
    else:
        dic[tree] += 1

total = sum(dic.values())

for tree_name, tree_cnt in sorted(dic.items()):
    print("%s %.4f" %(tree_name, (tree_cnt / total) * 100))


