from collections import Counter


def solution(participant, completion):
    answer = ''
    # 방법1. 교집합을 사용해서 같은 애들만 골라내는 작업 -> 동명이인이 있을 수 있어서 안된다.
    # 방법2. not in 사용 -> 시간초과
    # 방법3. sort, index

    # participant, completion =  sorted(participant), sorted(completion)
    
    # for i in range(len(completion)):
    #     if participant[i] != completion[i]:
    #         return participant[i]

    # hashDict = {}
    # sumHash = 0

    # for part in participant:
    #     hashDict[hash(part)] = part
    #     sumHash += hash(part)

    # for comp in completion:
    #     sumHash -= hash(comp)

    # return hashDict[sumHash]

    part_counter = Counter(participant)
    comp_counter = Counter(completion)

    answer = part_counter-comp_counter
    
    return list(answer.keys())[0]


solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])
