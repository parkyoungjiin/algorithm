t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())

    game = [[0] * (n+1) for _ in range(n+1)]
    print(game)

    # 8방향에 대한 좌표
    direction = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]

    # 기본 세팅(가운데에 값 넣어주기)
    # black(1) : (n//2,n//2+1), (n//2+1,n//2), white(2) : n//2, (n//2)+1

    # 흑돌(1)
    game[(n//2)+1][n//2] = 1
    game[n//2][(n//2)+1] = 1
    # 백돌(2)
    game[n//2][n//2] = 2
    game[(n//2)+1][(n//2)+1] = 2


    for tc in range(1, t+1):
        x, y, type = map(int, input().split())
        data = []
        # 8방향 탐색
        for i in range(8):
            dx, dy = direction[i]
            nx = x + dx
            ny = y + dy
            while True:
                # 범위 벗어난 경우
                if nx <= 0 or nx > n or ny <= 0 or ny > n:
                    data = []
                    break
                
                # 빈 칸 인경우
                if game[nx][ny] == 0:
                    data = []
                    break

                # 같은 돌 인 경우
                if game[nx][ny] == type:
                    break
                # 다른 돌 인경우
                else:
                    data.append((nx,ny))

                nx, ny = nx + dx, ny + dy
                
            # 다른 돌을 지금 돌로 변경
            for tx, ty in data:
                if type == 1:
                    game[tx][ty] = 1
                elif type == 2:
                    game[tx][ty] = 2
        game[x][y] = t 

    w_cnt, b_cnt = 0, 0
    for i in range(n):
        w_cnt += game[i].count(2)
        b_cnt += game[i].count(1)

    print(w_cnt, b_cnt)




            


        

        

