n = int(input())

# 666부터 ~ 10000까지
start = 666
cnt = 1
# cnt 가 n 이 될 때까지 반복.
while cnt != n:
    start += 1
    # start에 666이 들어 있으면 cnt 증가.
    if str(start).find('666') != -1:
        cnt += 1

print(start)

