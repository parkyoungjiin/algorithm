"""
프로그래머스 치킨은 치킨을 시켜먹으면 한 마리당 쿠폰을 한 장 발급합니다.
쿠폰을 열 장 모으면 치킨을 한 마리 서비스로 받을 수 있고, 서비스 치킨에도 쿠폰이 발급됩니다.
10 마리일 때 1마리 서비스(쿠폰+1)
시켜먹은 치킨의 수 chicken이 매개변수로 주어질 때 받을 수 있는 최대 서비스 치킨의 수를 return하도록 solution 함수를 완성해주세요.

"""
"""

def solution(chicken):
    coupon = 0
    service_chichken = 0
    for i in range(1, chicken+1):
        coupon += 1
        if coupon % 10 == 0:
            service_chichken += 1
            coupon += 1
        
    return service_chichken
"""

def solution(chicken):
    coupon = 0
    service_chicken = 0
    while chicken >= 10:
        #   
        div, mod = divmod(chicken, 10)
        service_chicken += div
        chicken = div+mod # 쿠폰이 서비스 치킨에도 있기에, 서비스 치킨 수만큼 나머지와 더해준다.

    print(div, mod)
    return coupon

solution(100)
solution(1081)
