def solution(n, lost, reserve):
    # 2 <= n <= 30
    # 1 <= lost <= n (중복 X)
    answer = 0
    new_lost = []
    for i in lost:
        # 여분 있는 학생이 잃어버린 경우
        if i not in reserve:
            new_lost.append(i)
        # 여분 없는 학생이 잃어버린 경우
        else:
            reserve.remove(i)
    # 학생 수 - 잃어버린 학생 수
    answer = n - len(new_lost)
    # 잃어버린 학생 중 reserve에서 빌릴 수 있는 경우 answer값에서 증가
    for lost_student in sorted(new_lost):
        # 앞, 뒷번호 학생만 빌릴 수 있음.
        if lost_student -1 in reserve:
            answer += 1
            reserve.remove(lost_student - 1)
        
        elif lost_student +1 in reserve:
            answer += 1
            reserve.remove(lost_student + 1)

    print("끝")
    return print(answer)

# solution(5, [2,4], [1,3,5])
solution(5, [4, 2], [3, 5])
solution(5, [3,4], [3])
# solution(3, [3], [1])