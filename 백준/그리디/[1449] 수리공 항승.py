N, L  = map(int,input().split())

S = list(map(int,input().split()))
# 정렬
S.sort()

count = 1

start = S[0]-1
end = start+L

for i in range(1,N):
    
    if S[i]<=end:
        continue
    # 끝점보다 크면 개수 증가
    else:
        count+=1
        start = S[i]-1
        end = start+L
        
print(count)