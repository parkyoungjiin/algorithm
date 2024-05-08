import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
block = []
for _ in range(n):
    block.append(list(map(int,input().split())))

answer = int(1e9)
glevel = 0
#모든 층 순회
for floor in range(257):
    # 사용한 블럭(1초), 가져온 블럭(2초)
    use_block, take_block = 0, 0

    for i in range(n):
        for j in range(m):
            if block[i][j] > floor:
                take_block += block[i][j] - floor
            else:
                use_block += floor - block[i][j]
        
    # 사용한 블럭이 (인벤토리 + 가져온 블럭) 보다 많은 경우 최종 연산을 하지 않음.
    if use_block > take_block + b:
        continue
    
    # 사용 블럭 < (인벤토리 + 가져온 블럭) 인 경우는 최종 연산

    count = (take_block * 2) + use_block

    if count <= answer:
        answer = count
        glevel = floor
    
print(answer, glevel)
            
