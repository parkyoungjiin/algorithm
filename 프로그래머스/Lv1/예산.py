def solution(d, budget):
    answer = 0
    # 예산에서 d에 있는 원소들을 하나씩 빼면서 answer 
    # 1. 기존 예산보다 작을 때만 작업 진행. (정렬 후 작은 값부터 빼주면 될듯)
    # 2. 
    d = sorted(d)
    
    for i in d:
        if budget >= i:
            budget -= i
            answer += 1

    return answer

solution([1,3,2,5,4], 9)
solution([2,2,3,3], 10)