import sys
input = sys.stdin.readline

n = int(input())

meetting = []

for _ in range(n):
    meetting.append(list(map(int, input().split())))

# 종료점 기준으로 정렬 -> 같을 때는 시작 시간이 빠른 순으로 정렬
meetting.sort(key=lambda x:(x[1], x[0]))

answer = 1 # 회의 최대 개수
s, e = meetting[0][0], meetting[0][1]
for i in range(1, n):
    start = meetting[i][0]
    if e <= start:
        answer += 1
        s, e = meetting[i][0], meetting[i][1]


print(answer)




