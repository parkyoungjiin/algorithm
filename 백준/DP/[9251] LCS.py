import sys
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()


lcs = [[0] * (len(str2)+1) for i in range(len(str1)+1)]

for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
        # 같은 문자인 경우 = 최대 부분 수열 + 1
        if str1[i-1] == str2[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        # 다른 문자인 경우 = max([i-1][j], [i][j-1])
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
print(lcs[len(str1)][len(str2)])


        


