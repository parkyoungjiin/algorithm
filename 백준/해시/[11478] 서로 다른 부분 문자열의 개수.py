import sys
input = sys.stdin.readline

s = input().rstrip()
s_len = len(s)
s_set = set()

for i in range(s_len):
    for j in range(i, s_len):
        s_set.add(s[i:j+1])

print(s_set)




# for i in range(s_len):
#     start_idx = 0
#     end_idx = i
#     while end_idx <= s_len:
#         s_set.add(s[start_idx:end_idx])
#         start_idx += 1
#         end_idx += 1
# print(s_set)
# print(len(s_set))





