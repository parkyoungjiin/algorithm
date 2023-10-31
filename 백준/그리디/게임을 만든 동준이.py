# 레벨
level_cnt = int(input())
level_list = []

# 몇 번 감소시켜야 하는 지
discount_cnt = 0

for _ in range(level_cnt):
    level_list.append(int(input()))

for i in range(level_cnt-2, -1, -1):
    if level_list[i] >= level_list[i+1]:
        discount_cnt += level_list[i] - level_list[i+1] + 1
        level_list[i] = level_list[i+1]-1
print(discount_cnt)

    

