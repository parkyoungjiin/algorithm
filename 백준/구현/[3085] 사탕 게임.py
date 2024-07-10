import sys
input = sys.stdin.readline

n = int(input())
def check():
    global answer
    # 같은 색의 개수 체크
    for i in range(n):
        # 가로
        cnt = 1
        for j in range(1, n):
            if board[i][j-1] == board[i][j]:
                cnt += 1
            else:
                cnt = 1
            answer = max(cnt, answer)

        # 세로
        cnt = 1
        for j in range(1, n):
            if board[j-1][i] == board[j][i]:
                cnt += 1
            else:
                cnt = 1
            answer = max(cnt, answer)
            

board = []
answer = 0
for _ in range(n):
    board.append(list(input().rstrip()))

for i in range(n):
    for j in range(n):
        # 오른쪽
        if j+1 < n and board[i][j] != board[i][j+1]:
            # 변경
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            check()
            # 원복
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

        # 아래
        if i+1 < n and board[i][j] != board[i+1][j]:
            # 변경
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            check()
            # 원복
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

            
print(answer)