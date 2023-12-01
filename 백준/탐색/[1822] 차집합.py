import sys
input = sys.stdin.readline

a, b = map(int, input().split())
list_a = set(map(int,input().split()))
list_b = set(map(int,input().split()))

# a - b

print(len(list_a - list_b))

print(*sorted(list(list_a - list_b)))



# 시간 초과
# temp = []
# for la in list_a:
#     if la not in list_b:
#         temp.append(int(la))

# if len(temp) > 0:
#     print(len(temp))
#     for t in temp:
#         print(t, end =' ')
# else:
#     print(0)

