def solution(brown, yellow):
    answer = []
    i = 1
    while i <= yellow:
        width = i
        if yellow % width == 0:
            height = yellow // width
            if (height + 2) * 2 + width * 2 == brown:
                answer.append(height+2)
                answer.append(width+2)
                break
        i += 1
    return answer