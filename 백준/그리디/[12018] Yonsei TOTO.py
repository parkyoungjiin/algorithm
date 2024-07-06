import sys

input = sys.stdin.readline

n, m = map(int, input().split())

ans = 0
l_lst = []
for i in range(n):
    p, l = map(int, input().split())
    m_lst = sorted(list(map(int, input().split())), reverse=True)

    if p < l:
        m -= 1
        ans += 1
    else:
        l_lst.append(m_lst[l-1])
l_lst.sort()
for i in range(len(l_lst)):
    if m - l_lst[i] < 0:
        break

    else:
        m = m - l_lst[i]+1
        ans += 1

print(ans)







