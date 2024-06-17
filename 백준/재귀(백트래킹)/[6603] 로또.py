import sys
input = sys.stdin.readline


def dfs(cnt, start, tlst):
    if cnt == 6:
        print(*tlst)
        return 
    # 재귀 포인트
    for i in range(start, k):
        # cnt = 로또 개수, i는 
        dfs(cnt+1, i+1, tlst+[s[i]])




while True:
    lst = list(map(int, input().split()))
    
    if lst[0] == 0:
        break

    k = lst[0]
    s = lst[1:]

    dfs(0, 0, [])
    print()


    
