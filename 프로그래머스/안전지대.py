"""
다음 그림과 같이 지뢰가 있는 지역과 지뢰에 인접한 위, 아래, 좌, 우 대각선 칸을 모두 위험지역으로 분류합니다.

지뢰 -> 2차원배열 board (지뢰 있으면 1, 없으면 0)
1을 기준으로 위, 아래, 좌, 우, 대각선 모두 위험
위 -> [-1],[0]
아래 -> [1][0]
왼 -> [0, -1]
오 -> [0, 1]
대각 -> [-1][-1], [-1][1], [1][-1], [1],[1]

안전한 지역 칸 수 return

1 기준으로 0위험지역으로 변경하기..

"""

from collections import deque


def solution(board):
    answer = 0
    # 왼, 오, 위, 아래, 위왼대각, 위오대각, 아래왼대각, 아래오대각
    dx = [0,0,-1,1,-1,-1,1,1]
    dy = [-1,1,0,0,-1,1,-1,1]
    length = len(board) 
    visited = [[False] * length for _ in range(length)]

    def dfs(x,y):
        dq = deque()
        dq.append((x,y))
        while dq:
            a,b = dq.popleft()
        print(a,b)
        visited[a][b] = True
        for i in range(8):
            nx = dx[i] + a
            ny = dy[i] + b
            if 0<=nx<length and 0<=ny<length and not visited[nx][ny]:
                if board[nx][ny] == 1:
                    dq.append((nx,ny))
                else:
                    board[nx][ny] = 2


    for i in range(length):
        for j in range(length):
            if board[i][j] == 1:
                dfs(i,j)
  
    return answer

solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]])

