"""
문자열 "hello"에서 각 문자를 오른쪽으로 한 칸씩 밀고 
마지막 문자는 맨 앞으로 이동시키면 "ohell"이 됩니다. 
이것을 문자열을 민다고 정의한다면 문자열 A와 B가 매개변수로 주어질 때,
- A를 밀어서 B가 될 수 있다면 밀어야 하는 최소 횟수를 return하고 
- 밀어서 B가 될 수 없으면 -1을 return 하도록 solution 함수를 완성해보세요.


"""
"""
1. --------인덱스 사용한 코드---------(내가 푼 코드)
def solution(A, B):
    answer = 0
    # A_str = ''
    # print(A[:-1])
    if A != B:
        for i in range(1, len(A)):
            A = A[-1] + A[:-1]
            print(A)
            if A == B:
                answer = i
                break
            else:
                answer = -1
    else:
        answer = 0    
    return print(answer)
"""

"""
2. ---------deque 이용한 코드-----------
from collections import deque


def solution(A, B):
    AList = deque(A)
    BList = deque(B)

    for i in range(len(AList)):
        if AList == BList:
            return i
        else:
            AList.rotate(1)
    return -1
"""

"""
3. -----------find() 이용-----------
find 함수 사용 시 찾는 문자열이 있다면 인덱스를 리턴함.
"""
def solution(A, B):
    B *= 2
    print(B)
    print(B.find(A))



solution("hello","ohell")
solution("apple", "leapp")
solution("atat", "tata")
solution("abc", "bca")

