n = int(input())
cnt = 0

# 첫 번째 단어를 입력받아 처리
first_word = ''.join(sorted(list(input())))

# 나머지 단어들을 입력받고 비교
for i in range(1, n):
    word = ''.join(sorted(list(input())))
    if first_word == word:
        cnt += 1

print(cnt)



