n = int(input())

time = sorted(list(map(int,input().split())))

result = 0
arr = []
for i in range(n):
    result += time[i]
    arr.append(result)

print(sum(arr))