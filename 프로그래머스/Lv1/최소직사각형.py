# 다시 풀어보기!
def solution(sizes):
    answer = 0
    w_max, h_max = 0,0
    for i,j in sizes:
        if i > j:
            i, j = j, i
        w_max = max(w_max,i)
        h_max = max(h_max,j)
    return print(w_max * h_max)



solution([[60, 50], [30, 70], [60, 30], [80, 40]])
solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])
