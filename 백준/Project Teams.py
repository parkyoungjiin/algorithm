# 팀 수
N = int(input())
# 코딩 역량(오름차순 정렬)
M = list(map(int, input().split()))
sort_M = sorted(M)

len_M = len(M)
# 팀의 역량을 담는 배열
total_M = []

for i in range(N):
    total_M.append(sort_M.pop(0) + sort_M.pop(-1)) 
print(min(total_M))
    
# 역량이 최소값 + 최솟값으로 팀을 이룬 값 중에 최소값 도출
