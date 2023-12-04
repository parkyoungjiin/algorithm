T = int(input())
for test_case in range(1, T + 1):
    game = ['3','6','9']
    answer_str = ''
    # answer_num = ''
    flag = False
    for t in str(test_case): 
        if t in game:
            answer_str += '-'
            flag = True
        # else:
        #     answer_num += t 
        
    if flag:
        print(answer_str, end =' ')
    else:
        print(test_case, end = ' ')
        