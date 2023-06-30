"""
다음 그림과 같이 지뢰가 있는 지역과 
지뢰에 인접한 위, 아래, 좌, 우 대각선 칸을 모두 위험지역으로 분류합니다.

지뢰는 2차원 배열 board에 1로 표시되어 있고 
board에는 지뢰가 매설 된 지역 1과, 지뢰가 없는 지역 0만 존재합니다.
지뢰가 매설된 지역의 지도 board가 매개변수로 주어질 때, 
안전한 지역의 칸 수를 return하도록 solution 함수를 완성해주세요.

"""
def solution(board):
    answer = 0
    # 위 아래 좌 우 좌위대각 우위대각 좌아래대각 우 아래대각
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    # 1(지뢰) 횟수만큼 담김.
    index = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                # 지뢰 위치 인덱스에 저장.
                index.append((i,j))
    print(index)
    
    for i in range(len(index)):
        x, y = index[i]
        for j in range(len(dx)):
            mx = x + dx[j]
            my = y + dy[j]
            print(mx, my)
            # board 범위를 설정하지 않으면 list assignment index out of range 에러가 발생함.
            # 0보다 크고, board 길이보다 작아야함. (인덱스이기에.)
            if 0 <= mx < len(board) and 0 <= my < len(board):
                board[mx][my] = 1

    for i in board:
        answer += i.count(0)
    
    return answer

    
    

    
solution([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]])