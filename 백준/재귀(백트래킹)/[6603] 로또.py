import sys
input = sys.stdin.readline

def dfs(start):
    global tlst
    if len(tlst) == 6:
        print(*tlst)
        return
    
    for i in range(start, len(s)):
        tlst.append(s[i])
        dfs(i+1)
        tlst.pop()
        
    
tlst = []
while True:
    tcase = list(map(int,input().split()))
    
    k, s = tcase[0], tcase[1:]
    
    if k == 0:
        break

    dfs(0)
    print()
    

    
