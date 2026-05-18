def solution(arr):
    answer = []
    q = []
    q.append(arr[0])
    answer.append(arr[0])
    for number in arr:
        a = q.pop()
        if a == number:
            q.append(number)
            continue
        else:
            q.append(number)
            answer.append(number)
    return answer