"""

지나다니는 길을 'O', 장애물을 'X'로 나타낸 직사각형 격자 모양의 공원에서 로봇 강아지가 산책을 하려합니다. 
산책은 로봇 강아지에 미리 입력된 명령에 따라 진행하며, 명령은 다음과 같은 형식으로 주어집니다.

["방향 거리", "방향 거리" … ]
예를 들어 "E 5"는 로봇 강아지가 현재 위치에서 동쪽으로 5칸 이동했다는 의미입니다.
 로봇 강아지는 명령을 수행하기 전에 다음 두 가지를 먼저 확인합니다.

주어진 방향으로 이동할 때 공원을 벗어나는지 확인합니다.
주어진 방향으로 이동 중 장애물을 만나는지 확인합니다.
위 두 가지중 어느 하나라도 해당된다면, 로봇 강아지는 해당 명령을 무시하고 다음 명령을 수행합니다.
공원의 가로 길이가 W, 세로 길이가 H라고 할 때, 공원의 좌측 상단의 좌표는 (0, 0), 우측 하단의 좌표는 (H - 1, W - 1) 입니다.

"""

def solution(park, routes): # 공원, 이동 명령어 -> [세로 좌표, 가로 좌표]
    answer = []
    row, col = len(park), len(park[0])
    # 이동 명령어 선언 (E W S N, 동서남북)
    op = {'E' : (0,1), 'W' : (0,-1), 'S' : (1,0), 'N':(-1,0)}
    x, y = 0, 0
    # 시작점 찾기
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                x, y = i, j
    # print(x, y)

    # routes에서 op, n 구분하기
    for route in routes:
        route_list = route.split()
        dx, dy = op[route[0]]
        count = int(route_list[1])
        
        xx, yy = x, y
        canmove = True

        for reply in range(count):
            mx, my = xx + dx, yy + dy
            # 장애물 있거나, 범위를 벗어나면 이동 못함.
            if 0<= mx <=row-1 and 0<=my<=col-1 and park[mx][my] != 'X':
                canmove = True
                # 이동 성공 시 mx값, my값을 xx, yy에 저장
                xx,yy = mx, my
            else:
                canmove = False
                break
        if canmove:
            x, y = mx, my

    return [x,y]


solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"])
solution(["OSO","OOO","OXX","OOO"], ["E 2","S 2","W 1"])