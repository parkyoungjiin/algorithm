from collections import Counter
import sys
 
input = sys.stdin.readline
t = int(input())
n = int(input())
n_list = list(map(int,input().split()))
m = int(input())
m_list = list(map(int,input().split()))

# 부배열 제작

sub_nlist = []
sub_mlist = []
cnt = 0
for i in range(n):
    sum = 0
    for j in range(i,n):
        sum += n_list[j]
        sub_nlist.append(sum)

for i in range(m):
    sum = 0
    for j in range(i,m):
        sum += m_list[j]
        sub_mlist.append(sum)

# 크기 순 배열, Counter 사용 -> Sum이 T

sub_nlist.sort()
sub_mlist.sort()

print(sub_nlist)
print(sub_mlist)
c = Counter(sub_mlist)
print(c)










"""
for i in range(n):
    sub_nlist.append(sum(n_list[:i+1]))
for i in range(m):
    sub_mlist.append(sum(m_list[:i+1]))
start, end = 0, m-1

while start < n:
    # 1 3 1 2
    # sub_nlist = [1 4 5 7]
    # 1 3 2
    # sub_mlist = [1 4 6]
    temp_sum = sub_nlist[start] + sub_mlist[end]
    if temp_sum == t:
        cnt += 1
        start += 1
        end = m-1
    if temp_sum > t:
        if end > 0:
            end = end -1
        elif end == 0:
            start += 1
            end = m-1
    elif temp_sum < t:
        start += 1
        end = m-1
    
    
print(cnt)
"""
        


