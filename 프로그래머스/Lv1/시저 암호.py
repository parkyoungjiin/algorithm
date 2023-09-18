def solution(s, n):
    answer = ''
    # 공백은 공백
    
    # 아스키코드로 변환
    # 대문자 65~90, 소문자 97~122
    for i in s:
        # 공백
        if i == " ":
            answer += i
        else:
            ord_val = chr(ord(i) + n)
            # 대문자
            if ord_val.isupper() != i.isupper() or not ord_val.isalpha():
                ord_val = chr(ord(ord_val) - 26)
            answer += ord_val
    return answer

# solution("AB",1)
# solution("z",1)
solution("a B z",25)

