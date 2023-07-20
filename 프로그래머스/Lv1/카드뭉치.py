from collections import deque


def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)

    for i in goal:
        if cards1:
            if i == cards1[0]:
                cards1.popleft()
            else:
                continue
    for i in goal:
        if cards2:
            if i == cards2[0]:
                cards2.popleft()
            else:
                continue
   
        
    if len(cards1) == 0 and len(cards2) == 0:
        answer = "Yes"
    else:
        answer = "No"

    return print(answer)
        


solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"])
solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"])
solution(["def", "bcd"], ["b", "c", "d"], ["bcd"])