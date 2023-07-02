def solution(babbling):
    cnt = 0
    words = ['aya', 'ye', 'woo','ma']
    for i in babbling:
        for j in words:
            i = i.replace(j, " ")
            if not i.strip():
                cnt += 1
                break

    return cnt