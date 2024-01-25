import sys
input = sys.stdin.readline

s, e, q = input().split()
dict = {}
answer = {}
# 입력 개수를 모를 때 처리
while True:
    try:
        time, nick = input().split()
        # 입장
        if time <= s:
            dict[nick] = time
        
        # 퇴장(개총 끝보다 크거나 같고, 스트리밍 보다 작거나 같은 경우)
        elif e <= time <= q:
            # 딕셔너리에 있는 경우 입장을 했다는 뜻이므로 answer에다가 넣어줌
            if nick in dict:
                answer[nick] = 1
    except:
        break

print(len(answer))


