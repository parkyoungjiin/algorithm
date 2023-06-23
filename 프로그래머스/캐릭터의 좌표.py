"""
머쓱이는 RPG게임을 하고 있습니다.
게임에는 up, down, left, right 방향키가 있으며 
각 키를 누르면 위, 아래, 왼쪽, 오른쪽으로 한 칸씩 이동합니다. 
예를 들어 [0,0]에서 up을 누른다면 캐릭터의 좌표는 [0, 1], down을 누른다면 [0, -1], left를 누른다면 [-1, 0], 
right를 누른다면 [1, 0]입니다.
머쓱이가 입력한 방향키의 배열 keyinput와 맵의 크기 board이 매개변수로 주어집니다. 
캐릭터는 항상 [0,0]에서 시작할 때 키 입력이 모두 끝난 뒤에 캐릭터의 좌표 [x, y]를 return하도록 solution 함수를 완성해주세요.

"""
def solution(keyinput, board):
    direction = ["left", "right", "up", "down"]

    x = [-1, 1, 0, 0]
    y = [0, 0, 1, -1]

    dx = 0
    dy = 0

    max_x = (board[0] - 1) //2
    min_x = -(board[0] -1) //2
    max_y = (board[1] - 1) //2
    min_y = -(board[1] - 1) //2

    for i in keyinput:
        keyIndex = direction.index(i)
        if dx + x[keyIndex] <= max_x and dx + x[keyIndex] >= min_x and dy + y[keyIndex] <= max_y and dy + y[keyIndex] >= min_y:
            dx += x[keyIndex]
            dy += y[keyIndex]
        else:
            continue
    print('dx', dx, 'dy:', dy)
    answer = []
    answer.append(dx)
    answer.append(dy)
    return answer


solution(["left", "right", "up", "right", "right"], [11,11])
solution(["down", "down", "down", "down", "down"],[7,9])


testArr = 123
print('test:',str(testArr)[:-1])
