# N 입력받기
import sys
input = sys.stdin.readline
    
T = int(input())

# 달팽이 방향으로 우하좌상 좌표 설정
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    N = int(input())
    # 2차원 행렬 제작.
    snail = [[0]*N for _ in range(N)]

    # 초기 위치 & 회전방향 설정
    r, c = 0, 0
    dist = 0  # 0:우, 1:하, 2:좌, 3:상

    # 1~10까지의 값 for 돌기
    for n in range(1, N*N + 1):
        snail[r][c] = n
        # 위치에 맞게 이동
        r += dr[dist]
        c += dc[dist]

        # 만약 범위를 벗어나거나 0이 아닌 다른 값이 있다면 방향 전환!
        if r < 0 or c < 0 or r >= N or c >= N or snail[r][c] != 0:
        # if r < 0 or c < 0 or snail[r][c] != 0 or r < N or c < N:
            # 실행취소
            r -= dr[dist]
            c -= dc[dist]
            # dist는 % 4 안해주면 0123, 4567, ... 이런식으로 숫자 커지므로 나머지로 접근
            dist = (dist + 1) % 4
            #  다시 좌표 계산
            r += dr[dist]
            c += dc[dist]
    
    print("#{}".format(tc))
    for row in snail:
        # 리스트 변수에 * 붙이면 [] 제거하고 출력.
        print(row)
    print()

                

