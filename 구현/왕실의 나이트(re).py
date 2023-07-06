cnt = 0
# 현재 위치 입력 받기(행, 열)
# - 행은 숫자, 열은 알파벳
night = input()
x, y = night[1], ord(night[0])
# print(x,y)
limit_x, limit_y = 8, ord('h')
# 이동 방법
step = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]

# 이동
for i,j in step:
    # print(i,j)
    # 범위를 벗어날 경우
    if int(x) + i > limit_x or int(x) + i <= 0 or int(y) + j > limit_y or int(y) + j <= 0:
        continue
    else:
        cnt += 1

print(cnt)
