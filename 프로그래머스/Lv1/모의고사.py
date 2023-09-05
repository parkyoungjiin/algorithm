def solution(answers):
    # 1,2,3번 수포자 정답 찍는 방식
    student1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    # return 결과
    result = []
    # 정답 체크 결과 담을 배열
    score = [0,0,0]
    # 정답 체크
    for index, answer in enumerate(answers):
        # len으로 나머지 연산자 사용하는 것이 포인트.
        if student1[index%len(student1)] == answer:
            score[0] += 1

        if student2[index%len(student2)] == answer:
            score[1] += 1

        if student3[index%len(student3)] == answer:
            score[2] += 1
    # score 중 가장 높은 점수를 가진 사람을 append, 모두 같을 경우 오름차순.
    for index, score_value in enumerate(score):
        if score_value == max(score):
            ap_index = index+1
            result.append(ap_index)
    
    return result


solution([1,2,3,4,5,2,2,2,4,5])
solution([1,3,2,3,2])