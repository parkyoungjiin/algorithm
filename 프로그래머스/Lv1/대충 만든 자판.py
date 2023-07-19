def solution(keymap, targets):
    answer = []
    answer_val = 0
    keymap_dict = {}
    # targets의 요소들을 하나씩 꺼내어 keymap에서 탐색? in을 통해 찾은 후 인덱스가 낮은 번호를 더한다.
    for i in keymap:
        for index, value in enumerate(i):
            check_val = keymap_dict.get(value, "")
            # 기존의 index값과 
            if check_val == "":
                keymap_dict[value] = index+1

            else:
                # 기존의 value와 index를 비교하여 적은 값을 dict에 넣는다.
                if check_val <= index:
                    continue
                else:
                    keymap_dict[value] = index+1
    
    for target in targets:
        for t in target:
            # 존재 여부 확인 없으면 answer는 -1
            # 있으면 value값을 answer에 증감함.
            if keymap_dict.get(t,"") == "":
                answer_val = -1
                break
            else:
                answer_val += keymap_dict[t]
        answer.append(answer_val)
        answer_val = 0


             
    return print(answer)

solution(["ABACD", "BCEFD"], ["ABCD","AABB"])
solution(["AA"], ["B"])
solution(["AGZ", "BSSS"], ["ASA","BGZ"]	)
solution( ["ABCE"], ["ABDE"])

"""

단, 목표 문자열을 작성할 수 없을 때는 -1을 저장합니다.


 
"""