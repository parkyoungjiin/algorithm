def solution(num, lim, pow):
    div = [1]
    for i in range(2, num+1):
        cnt = 0
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1
        if cnt > lim:
            cnt = pow
            div.append(cnt)
        else:    
            div.append(cnt)
    return (sum(div))