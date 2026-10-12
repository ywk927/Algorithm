def solution(n):
    answer = 0
    for i in range(1, n+1):
        k = i
        f = 1
        while True:
            if k == n:
                answer += 1
                f = 1
                break
            elif k > n:
                f = 1
                break
            else:
                k += i + f
                f += 1
    return answer