"""
PROGRAMMERS-962 행성에 불시착한 우주비행사 머쓱이는 외계행성의 언어를 공부하려고 합니다. 
알파벳이 담긴 배열 spell과 외계어 사전 dic이 매개변수로 주어집니다. 
spell에 담긴 알파벳을 한번씩만 모두 사용한 단어가 dic에 존재한다면 1, 존재하지 않는다면 2를 return하도록 solution 함수를 완성해주세요.

# dic에 있는 문자열, spell에 있는 문자 하나씩 비교하여 일치하면 cnt를 증가시킴.
# 증가한 값이 같을 경우 1 아니면 2

"""


"""
def solution(spell, dic):
    answer = 0
    # 1. 오름차순 정렬 후 문자열로 결합.
    spell = "".join(sorted(spell))
    print('spell:',spell)

    # 2. dic의 요소들 하나하나씩을 똑같이 오름차순 정렬 후에 문자열로 결합하여 리스트에 저장.
    for i in dic:
        index = dic.index(i)
        dic[index] = "".join(sorted(i))
    print(dic)

    for i in dic:
        if i == spell:
            answer = 1
            break
        else:
            answer = 2
    return answer
"""

def solution(spell, dic):
    spell = set(spell)
    print("spell",spell)

    for s in dic:
        if not spell-set(s):
            return 1
    return 2



solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"])
solution(["z", "d", "x"],["def", "dww", "dzx", "loveaw"])

