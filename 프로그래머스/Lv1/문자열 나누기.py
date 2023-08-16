def solution(s):
    answer = 0
    # x와 동일한 횟수, x와 다른 횟수
    cnt1 , cnt2 = 0,0

    for i in s:
       if cnt1==cnt2:
           answer+=1
           k=i
       if k==i:
           cnt1+=1
       else:
           cnt2+=1
       
    return answer

solution("banana")
solution("abracadabra")

