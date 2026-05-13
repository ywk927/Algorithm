from collections import deque
def solution(tickets):
    true_answer = ['ZZZ']
    answer = []
    i = 1
    for ticket in tickets:
        ticket.append(i)
        i += 1
    n = len(tickets)
    def bfs(index, route, visited):
        nonlocal answer
        if index == n:
            if len(route) == n+1:
                answer.append(route[:])
            return
        start = route[-2]
        end = route[-1]
        for k in range(n):
            if tickets[k][0] == end and visited[k+1] == 0:
                visited[k+1] = 1
                route.append(tickets[k][1])
                bfs(index+1, route, visited)
                route.pop()
                visited[k+1] = 0
    for x, y, z in tickets:
        if x == 'ICN':
            visited = [0 for _ in range(n+1)]
            visited[z] = 1
            bfs(1,[x, y], visited)
    for route in answer:
        true_answer = min(route, true_answer)
    return true_answer