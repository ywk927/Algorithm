def solution(numbers, hand):
    answer = ''
    arr = [["1","2","3"], ["4","5","6"],["7","8","9"],["*","0","#"]]
    current_left = [3,0]
    current_right = [3,2]
    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            answer += 'L'
            if number == 1:
                current_left = [0,0]
            elif number == 4:
                current_left = [1,0]
            elif number == 7:
                current_left = [2,0]
        elif number == 3 or number == 6 or number == 9:
            answer += 'R'
            if number == 3:
                current_right = [0,2]
            elif number == 6:
                current_right = [1,2]
            elif number == 9:
                current_right = [2,2]
        else:    
            for i in range(4):
                for j in range(3):
                    if arr[i][j] == str(number):
                        distance1 = abs(current_left[0] - i) + abs(current_left[1] - j)
                        distance2 = abs(current_right[0] - i) + abs(current_right[1] - j)
                        if distance1 > distance2:
                            answer += 'R'
                            current_right = [i,j]
                        elif distance1 < distance2:
                            answer += 'L'
                            current_left = [i,j]
                        else:
                            if hand == "left":
                                answer += 'L'
                                current_left = [i,j]
                            else:
                                answer += 'R'
                                current_right = [i,j]
                        break
        # print(number, current_left, current_right)
    return answer