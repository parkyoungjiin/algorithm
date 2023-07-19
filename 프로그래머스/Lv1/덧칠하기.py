def solution(n, m, sections):
    # n은 길이 ,m은 롤러 길이, section은 재페인트 구역
    # n은 범위 설정(벗어나면 안된다.)
    cnt = 1 # 최소 횟수
    scope = sections[0] + (m-1) # 칠해진 영역
    for i in range(len(sections)):
        # 만약 칠해진 영역이라면 cnt를 증가시키지 않음.
        if sections[i] <= scope:
            continue
        
        cnt += 1
        # 새로 칠해지는 범위 설정
        scope = sections[i] + (m-1)
        if scope > sections[-1]:
            break



    return cnt

# solution(8, 4, [2, 3,5,6])
solution(5, 4, [1,2])
solution(4, 1, [1,2,3,4])
# solution(4, 2, [3,4])