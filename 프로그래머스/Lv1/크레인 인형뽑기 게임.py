def solution(board, moves):
    answer = 0
    basket = []
    for move in moves:
        # 열(index)
        index = move - 1
        # 어느 칸이 비어있는 지 조회.
        for row_info in board:
            if row_info[index] != 0:
                basket.append(row_info[index])
                # basket에 담은 경우 0으로 초기화.
                row_info[index] == 0   
                
                if len(basket) >=2 and basket[-1] == basket[-2]:
                    answer += 2
                    basket = basket[0:-2]
                break
    return answer

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])