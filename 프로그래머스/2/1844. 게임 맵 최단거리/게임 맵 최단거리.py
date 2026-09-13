from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    answer = 0
    q = deque([])
    q.append([0,0])
    while q:
        ti, tj = q.popleft()
        if ti == n-1 and tj == m-1:
            break
        for di, dj in [[0,1], [1,0], [-1,0], [0,-1]]:
            ni, nj = ti+di, tj+dj
            if 0<= ni < n and 0<= nj < m and visited[ni][nj] == 0 and maps[ni][nj] == 1:
                visited[ni][nj] += visited[ti][tj] + 1
                q.append([ni, nj])
    if visited[n-1][m-1] == 0:
        answer = -1
    else:
        answer = visited[n-1][m-1]
    return answer