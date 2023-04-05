# 거스름돈 (그리디)
n = int(input())
count = 0
# 500원 ,100원, 50원, 10원 리스트에 저장
# 금액 / 코인타입 = 코인개수 , 금액 % 코인타입 = 나머지금액

coin_type = [500, 100, 50, 10]

for coin in coin_type:
    count += n // coin
    n %= coin


