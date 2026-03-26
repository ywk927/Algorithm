def solution(n):
    answer = 0

    col_used = [0] * n
    diag1_used = [0] * (2 * n)   # i - j + n
    diag2_used = [0] * (2 * n)   # i + j

    def check(i, j):
        if col_used[j] == 1:
            return False
        if diag1_used[i - j + n] == 1:
            return False
        if diag2_used[i + j] == 1:
            return False
        return True

    def backtrack(i):
        nonlocal answer

        if i == n:
            answer += 1
            return

        for j in range(n):
            if check(i, j):
                col_used[j] = 1
                diag1_used[i - j + n] = 1
                diag2_used[i + j] = 1

                backtrack(i + 1)

                col_used[j] = 0
                diag1_used[i - j + n] = 0
                diag2_used[i + j] = 0

    backtrack(0)
    return answer
n = int(input())
print(solution(n))