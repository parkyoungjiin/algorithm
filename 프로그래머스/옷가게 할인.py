# 머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다.
# 구매한 옷의 가격 price가 주어질 때, 지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.

"""
def solution(price):
    answer = 0
    if(price >= 500000):
        answer = int(price - (price * 0.2))
    elif(price >= 300000 and price < 500000):
        answer = int(price - (price * 0.1))
    elif(price >=100000 and price < 300000):
        answer = int(price - (price * 0.05))
    else:
        answer = int(price)
    return answer
"""

# 다른 사람의 풀이
def solution(price):
    discount_rates= {500000: 0.2, 300000: 0.1, 100000: 0.05}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price * discount_rate)






solution(100000)
solution(580000)