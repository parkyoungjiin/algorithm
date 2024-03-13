# https://thingjin.tistory.com/entry/%EB%B0%B1%EC%A4%80-11053%EB%B2%88-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC
n = int(input())
arr = list(map(int, input().split()))

# i가 0일 때 증가하는 최대 부분 수열의 길이는 1이기 때문에, 테이블을 우선 전부 1로 초기화해줌
d = [1] * n

for i in range(1, n): # 1부터 n - 1번 인덱스까지의 모든 i에 대하여
    for j in range(i): # i보다 작은 j 각각에 대해
        if arr[j] < arr[i]: # j의 원소가 i의 원소보다 작다면, 즉 부분적으로 증가한다면
            d[i] = max(d[i], d[j] + 1) # i에서의 최적의 해를 갱신해준다.

print(max(d)) # 가장 긴 증가하는 부분 수열의 길이 출력
print(d)