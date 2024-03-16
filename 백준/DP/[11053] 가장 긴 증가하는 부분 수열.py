# https://thingjin.tistory.com/entry/%EB%B0%B1%EC%A4%80-11053%EB%B2%88-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC
n = int(input())
arr = list(map(int, input().split()))
result = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(0, i):
        if arr[i] > arr[j]:
            result[i] = max(result[j]+1, result[i])
    

print(max(result))