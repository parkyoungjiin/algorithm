# def solution(k, score):
#     # k = 개수, score 의 개수는 일차.
#     # 최하위 점수를 answer에 넣어야 함.
#     answer = []
#     temp = []
#     for i in score:
#         # 길이가 같아지면 정렬을 한 후에 temp의 가장 적은 값과 비교한다.
#         if len(temp) == k:
#             if temp[0] < i:
#                 temp[0] = i
#                 temp = sorted(temp)
#                 answer.append(temp[0])
#             else:
#                 answer.append(temp[0])
#                 continue
#         else:
#             temp.append(i)
#             temp = sorted(temp)
#             answer.append(temp[0])

#     return answer


# -----다른 풀이--------

def solution(k, score):
    temp = []
    answer = []

    for i in score:
        temp.append(i)
        if len(temp) > k:
            temp.remove(min(temp))
        answer.append(min(temp))
    print(answer)
    return answer


solution(3, [10, 100, 20, 150, 1, 100, 200])