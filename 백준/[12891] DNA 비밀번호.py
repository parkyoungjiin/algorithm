import sys
input = sys.stdin.readline

s, p = map(int, input().split()) # s = 문자열 길이, p 는 부분 문자열

dna = list(input())

dna_min_list = list(map(int, input().split()))

count = 0

current_count = [0,0,0,0]

#초기 윈도우 설정
for i in range(p):
    if dna[i] == 'A':
        current_count[0] += 1
    elif dna[i] == 'C':
        current_count[1] += 1
    elif dna[i] == 'G':
        current_count[2] += 1
    elif dna[i] == 'T':
        current_count[3] += 1

# 초기 윈도우 조건 만족 확인
def check():
    for i in range(4):
        if current_count[i] < dna_min_list[i]:
            return False
    return True

if check():
    count += 1

# 슬라이딩 윈도우
for i in range(p, s):
    # 끝부분을 + 연산
    if dna[i] == 'A':
        current_count[0] += 1
    elif dna[i] == 'C':
        current_count[1] += 1
    elif dna[i] == 'G':
        current_count[2] += 1
    elif dna[i] == 'T':
        current_count[3] += 1
    # 앞부분 - 연산
    if dna[i - p] == 'A':
        current_count[0] -= 1
    elif dna[i - p] == 'C':
        current_count[1] -= 1
    elif dna[i - p] == 'G':
        current_count[2] -= 1
    elif dna[i - p] == 'T':
        current_count[3] -= 1

    # 현재 암호가 조건에 만족하는지 검사
    if check():
        count += 1

print(count)
