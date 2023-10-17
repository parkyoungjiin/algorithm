def solution(phone_number):
    num = len(phone_number)
    # 뒤 4자리 제외한 번호 저장.
    back = phone_number[-4:]
    # 리턴 시 길이 -4 만큼 *를 붙이고 표시할 번호 return
    return "*"*(num-4)+back