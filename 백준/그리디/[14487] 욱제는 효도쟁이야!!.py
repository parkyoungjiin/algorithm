# 마을 개수
N = int(input())

# 이동 비용
move_cost = list(map(int, input().split()))
max_cost = max(move_cost)
# 큰 값 찾은 후 제거하여 남은 값들 더하기.
move_cost.remove(max_cost)

print(sum(move_cost))

# 1 6 5 2 4
# 1-2 : 1, 2->3: 6, 3->4: 5, 4->5: 2, 5->1: 4
