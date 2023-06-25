"""
문자열 my_string이 매개변수로 주어집니다. my_string은 소문자, 대문자, 자연수로만 구성되어있습니다. 
my_string안의 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

조건1. 연속된 수는 하나의 숫자로 간주한다.
- how 구현하지..
    - 인덱스번지 활용?
    - 앞 뒤가 숫지인지 확인?
조건2. 문자열에 자연수가 없는 경우는 0으로 return


풀이 -> 나는 isnumeric을 사용하려 했는데, 
풀이를 보니 alpha를 사용하여 알파벳인 경우 공백으로 처리한 후 split을 통해 숫자만 리스트에 담은 후 sum하여 처리하였음. (조건2도 자동처리됨.)
"""

def solution(my_string):
    answer = []
    for i in my_string:
        if i.isalpha():
            my_string = my_string.replace(i, ' ')
    my_string = my_string.split()
    return print(sum(list(map(int,my_string))))

solution("aAbBcCop")
