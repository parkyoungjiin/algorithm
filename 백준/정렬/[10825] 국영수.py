import sys
input = sys.stdin.readline
N = int(input())

li = [input().strip().split() for _ in range(N)]

# 국어 기준 내림차순 - 영어 오름차순 - 수학 내림차순 - 이름 오름차순
# 파이썬에서 내림차순은 -를 붙여주고 오름차순은 안붙이면 정렬된다
li.sort(key = lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in li:
    print(i[0])





