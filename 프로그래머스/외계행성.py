"""
a : 0 ~ j : 9
age(정수형) -> 한 자리씩 판별하여 영어로 변환해줘야 함.
1. 매개변수 리스트로 변환
2. dict 사용하여 판별할 리스트 만들기
"""
def solution(age):
    dict = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9}
    print('get(key) :',dict.get('a'))
    list_age = list(map(int, str(age)))
    
    answer = ''
    for i in list_age:
        for key, value in dict.items():
            if value == i:
                answer += key
    
    return answer

solution(23)
solution(51)
solution(100)


def solution2(age):
    # 숫자 문자열 변환
    age = str(age)
    # 한 자리씩 반복문으로 출력 가능
    for i in age:
        print(i)
    return print(age)

solution2(23)