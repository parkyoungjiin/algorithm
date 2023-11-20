import sys
# 입력
N = int(sys.stdin.readline())
listN = []
for _ in range(N):
    listN.append(int(sys.stdin.readline()))

# 정렬(내림차순)
listN = sorted(listN,reverse=True)

# 출력
for i in listN:
    print(i)
