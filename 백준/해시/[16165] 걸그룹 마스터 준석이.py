import sys

input = sys.stdin.readline

n, m = map(int, input().split())
group = {}
for _ in range(n):
    group_name = input().rstrip()
    group_cnt = int(input())
    if group_name not in group.keys():
        member_list = []
        for _ in range(group_cnt):
            member = input().rstrip()
            member_list.append(member)
            group[group_name] = member_list


for _ in range(m):
    name = input().rstrip()
    type = int(input())
# 0 -> 그룹, 1 -> 멤버
    if type == 0:
        for n in sorted(group[name]):
            print(n)
    elif type == 1:
        for key, val in group.items():
            if name in val:
                print(key)





