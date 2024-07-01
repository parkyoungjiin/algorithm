math_lst = input().split('-')

num = []

for i in math_lst:
    temp = i.split('+')
    sum = 0
    for v in temp:
        sum += int(v)
    
    num.append(sum)

ans = num[0]
for n in range(1, len(num)):
    ans -= num[n]

print(ans)


