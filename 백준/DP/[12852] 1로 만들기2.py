import sys
input = sys.stdin.readline

n = int(input())
# dp = [[연산횟수, [1로 되는 숫자들]]]
dp = [[0, []] for _ in range(n+1)]
dp[1][0] = 0
dp[1][1] = [1]


for i in range(2, n+1):
    dp[i][0] = dp[i-1][0] + 1
    # 리스트 + 리스트 -> 두 리스트를 합쳐서 새로운 리스트를 반환하기에 두 리스트는 변경되지 않는다.
    # append는 현재 리스트에 새로운 요소를 추가하는 것이기에 현재 리스트가 변경된다.
    dp[i][1] = dp[i-1][1] + [i]

    if i % 3 == 0 and dp[i//3][0] + 1 < dp[i][0] :
        dp[i][0] = dp[i//3][0] + 1
        dp[i][1] = dp[i//3][1] + [i]
    
    if i % 2 == 0 and dp[i//2][0] + 1 < dp[i][0] :
        dp[i][0] = dp[i//2][0] + 1
        dp[i][1] = dp[i//2][1] + [i]
    
print(dp)



