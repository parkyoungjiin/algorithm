from collections import deque

# 문서 (0<=len<=2500)
# 소문자, 공백
doc = input()
# 찾는 단어(len<=50)
find_word = input()
index = 0
cnt = 0
for i in range(len(doc)):
    if index > i:
        continue
    if find_word == doc[i:i+len(find_word)]:
        # print("i체크:",i)
        # print("단어:",doc[i:i+len(find_word)])
        cnt += 1
        index = i + len(find_word)

print(cnt)



