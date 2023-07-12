"""
내가 짠 코드 밑에는
list, map 사용한 다른 사람의 풀이

def solution(strlist):
    answer =[]
    for i in(strlist):
        answer.append(len(i))
    return print(answer)
"""
def solution(strlist):
    answer = list(map(len,strlist))
    return print(answer)
solution(["We", "are", "the", "world!"]	)