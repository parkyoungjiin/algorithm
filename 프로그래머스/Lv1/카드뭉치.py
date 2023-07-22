from collections import deque


def solution(cards1, cards2, goal):
    cards1, cards2 = deque(cards1), deque(cards2)
    for i in goal:
        if len(cards1) and i == cards1[0]:
            cards1.popleft()
        elif len(cards2) and i == cards2[0]:
            cards2.popleft()
        else:
            return 'No'     
    return 'Yes'


# solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"])
solution(["i", "drink", "water"], ["drink", "water"],  ["i", "drink", "water"])
# solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"])
# solution(["def", "bcd"], ["b", "c", "d"], ["bcd"])