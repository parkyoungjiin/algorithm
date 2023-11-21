import sys
input = sys.stdin.readline

word = input().strip()
suffix_list = []
# 슬라이싱문제.
for i in range(len(word)):
    suffix_list.append(word[i:])
suffix_list.sort()

for suffix in suffix_list:
    print(suffix)
    


