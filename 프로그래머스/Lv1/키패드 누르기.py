def solution(numbers, hand):
    answer = ''
    # 키패드 좌표 선언
    keypad_location = {1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1], 9:[2,2], '*':[3,0], 0:[3,1], '#':[3,2]}
    
    # 왼손, 오른손 으로 누를 숫자 선언
    Left_location, Right_location = [1,4,7], [3,6,9]
    # 왼, 오 엄지손가락 시작 위치
    L_initial_location, R_initial_location = keypad_location['*'], keypad_location['#']

    for i in numbers:
        # 1,4,7 인 경우
        if i in Left_location:
            answer += 'L'
            L_initial_location = keypad_location[i]
        # 3,6,9 인 경우
        elif i in Right_location:
            answer += 'R'
            R_initial_location = keypad_location[i]
        # 2,5,8,0 인 경우
        else:
            # 왼쪽, 오른쪽 길이 계산
            left_distance = abs(keypad_location[i][0] - L_initial_location[0]) + abs(keypad_location[i][1] - L_initial_location[1])
            right_distance = abs(keypad_location[i][0] - R_initial_location[0]) + abs(keypad_location[i][1] - R_initial_location[1])

            if left_distance > right_distance: # 오른쪽이 가까운 경우
                answer += 'R'
                R_initial_location = keypad_location[i]
            elif left_distance < right_distance: # 왼쪽이 가까운 경우
                answer += 'L'
                L_initial_location = keypad_location[i]
            else: # 같은 경우
                # 오른손잡이
                if hand == "right":
                    answer += 'R'
                    R_initial_location = keypad_location[i]
                # 왼손잡이
                else:
                    answer += 'L'
                    L_initial_location = keypad_location[i]

    return answer

solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")