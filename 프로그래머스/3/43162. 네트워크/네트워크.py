def solution(n, computers):
    answer = 0
    true_visit = [0 for _ in range(n)]
    def dfs(current):
        true_visit[current] = 1
        for next_computer in range(n):
            if computers[current][next_computer] == 1 and true_visit[next_computer] == 0:
                dfs(next_computer)
    for i in range(n):
        if true_visit[i] == 0:
            answer += 1
            dfs(i)
    return answer