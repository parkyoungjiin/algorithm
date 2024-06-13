n = int(input())
answer = 0

first_word = list(input()) # 첫 단어

for _ in range(n-1):
    # print(first_word[:])
    target = first_word[:] # 복사
    compare_word = input()
    # print(compare_word)
    cnt = 0

    for w in compare_word:
        if w in target:
            target.remove(w)
        else:
            cnt+=1
    if cnt < 2 and len(target) < 2:
        answer += 1
print(answer)




