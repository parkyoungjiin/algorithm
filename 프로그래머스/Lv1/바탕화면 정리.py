def solution(wallpaper):
    answer = [] # return은 시작, 끝 좌표
    # temp_answer = []
    x_arr, y_arr = [], []
     
    # 시작점, 끝점 찾기
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                x_arr.append(i)
                y_arr.append(j)
    print("x", x_arr)
    print("y", y_arr)
    
    # print(temp_answer)
    # for i in range(len(temp_answer)):
    #     x_arr.append(temp_answer[i][0])
    #     y_arr.append(temp_answer[i][1])

    # answer.append(min(x_arr))
    # answer.append(min(y_arr))
    # answer.append(max(x_arr)+1)
    # answer.append(max(y_arr)+1)
    # print(min(x_arr), min(y_arr)) # 시작
    # print(max(x_arr)+1, max(y_arr)+1) # 끝점


    return print([min(x_arr), min(y_arr), max(x_arr)+1, max(y_arr)+1])


solution([".#...", "..#..", "...#."])
solution(["..........", ".....#....", "......##..", "...##.....", "....#....."])
solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."])