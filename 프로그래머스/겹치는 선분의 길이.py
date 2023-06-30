"""
선분 3개가 평행하게 놓여 있습니다. 세 선분의 시작과 끝 좌표가 
[[start, end], [start, end], [start, end]] 
형태로 들어있는 2차원 배열 lines가 매개변수로 주어질 때, 
두 개 이상의 선분이 겹치는 부분의 길이를 return 하도록 solution 함수를 완성해보세요.

lines가 [[0, 2], [-3, -1], [-2, 1]]일 때 그림으로 나타내면 다음과 같습니다.

선분이 두 개 이상 겹친 곳은 [-2, -1], [0, 1]로 길이 2만큼 겹쳐있습니다.

lines[a,b] => -100 ≤ a < b ≤ 100


범위문제

"""
"""
--------범위로 풀려했으나 풀리지 않음...---------
def solution(lines):
    answer = 0
    for i in range(len(lines)):

        x,y = lines[i][0], lines[i][1]
        print('x:',x,'y:',y)
        # 0번지일 때 1번지, 2번지
        if i == 0:
            if x <= lines[i+1][0] <= y or x <= lines[i+1][1] <= y:
                answer = abs(lines[i+1][0]) - abs(y)
            elif x <= lines[i+2][0] <= y or x <= lines[i+2][1] <= y:
                answer = abs(lines[i+2][0]) - abs(y)
        # 1번지일 때 0번지, 2번지
        elif i == 1:
            if x <= lines[i-1][0] <= y or x <= lines[i-1][1] <= y:
                answer = abs(lines[i-1][0]) - abs(y)
            elif x <= lines[i+1][0] <= y or x <= lines[i+1][1] <= y:
                answer = abs(lines[i+1][0]) - abs(y)
        # 2번지일 때 0번지, 1번지
        else:
            if x <= lines[i-2][0] <= y or x <= lines[i-2][1] <= y:
                answer = abs(lines[i-2][0]) - abs(y)
            elif x <= lines[i-1][0] <= y or x <= lines[i-1][1] <= y:
                answer = abs(lines[i-1][0]) - abs(y)

    return print(answer)
"""

"""

def solution(lines):
    answer = 0
    count = [0 for _ in range(200)] # 리스트 초기화 (-100 ~ 100)
    # 리스트에 범위 내 숫자를 카운트해주기 위해 리스트 선언.
    for line in lines:
        print(line)
        for i in range(line[0], line[1]):
            count[i + 100] += 1
    answer += count.count(2)
    answer += count.count(3)
    # print(count)
    return print(answer)

"""

def solution(lines):
    # table에 선분을 긋기 위해 선언함.
    table = [set([]) for _ in range(200)]
    for index, line in enumerate(lines):
        x1, x2 = line
        for x in range(x1, x2):
            table[x + 100].add(index)

    # 그여진 선분 횟수를 통해서 2번 이상 겹칠 경우를 출력하기에 반복문을 통해 출력함.
    count = 0
    for line in table:
        if len(line) > 1:
            count += 1
    return count
# solution([[0, 2], [-3, -1], [-2, 1]])
# solution([[0, 1], [2, 5], [3, 9]])
# solution([[-1, 1], [1, 3], [3, 9]])
solution([[0, 5], [3, 9], [1, 10]])