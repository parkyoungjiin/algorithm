def solution(board, moves):
    answer = 0
    stack = []
    # 1. moves의 원소를 하나씩 꺼내서 board 인덱싱으로 접근.
    for move in moves:
        move_index = move-1
        # stack에 넣는 작업.
        for b in board:
            if b[move_index] != 0:
                # print("확인", move_index, b[move_index])
                stack.append(b[move_index])
                b[move_index] = 0
                break
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            for i in range(2):
                stack.pop()
            answer += 2
    
    return answer


solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4])