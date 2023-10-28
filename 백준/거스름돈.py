s = int(input())
money = 1000
answer = 0
# 거스름돈
mod = money - s
# 화폐 종류
money_type = [500, 100, 50, 10, 5,1]

for m in money_type:
    if int(mod) >= int(m):
        answer += mod // m
        mod = mod % m

print(answer)
    



