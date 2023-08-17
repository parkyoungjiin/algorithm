def solution(k, m, score):
    # k = 최고등급, m = 한 상자에 담기는 개수

    benefit = 0
    score.sort(reverse=True)
    print(score)
    for i in range(0, len(score),m):
        temp = score[i:i+m]
        if len(temp) == m:
            min_score = min(temp)
            benefit += min_score * m
    return print(benefit)


solution(3,4,[1, 2, 3, 1, 2, 3, 1])
solution(4,3,[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2])



