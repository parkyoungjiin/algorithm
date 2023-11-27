import sys
input = sys.stdin.readline

N = int(input())
dict_card = {}
for i in range(N):
    card = int(input())
    # 값을 바로 dict에 넣어서 for를 2번 사용하지 않기에 시간 초과가 발생하지 않음.
    if card in dict_card:
        dict_card[card] += 1
    else:
        dict_card[card] = 1
    
# print(dict_cart)

# 가장 많이 가진 정수를 출력.
# 가장 많이 가진 정수가 여러 개 인경우는 적은 값을 출력한다.
# value 기준 정렬 -> key 기준 정렬 -> 0번지 key값 출력.

dict_card = sorted(dict_card.items(), key=lambda x:(-x[1],x[0]))
print(dict_card[0][0])

# set을 지워도 46퍼에서 멈춤. (시간초과)


# ---시간초과----
# N = int(input())

# card = []
# for _ in range(N):
#     card.append(int(input()))
# # print(card)
# set_cart = set(card)

# dict_cart = {}

# for s in set_cart:
#     dict_cart[s] = card.count(s)
# # print(dict_cart)

# # 가장 많이 가진 정수를 출력.
# # 가장 많이 가진 정수가 여러 개 인경우는 적은 값을 출력한다.
# # value 기준 정렬 -> key 기준 정렬 -> 0번지 key값 출력.

# dict_cart = sorted(dict_cart.items(), key=lambda x:(-x[1],x[0]))
# print(dict_cart[0][0])
    

