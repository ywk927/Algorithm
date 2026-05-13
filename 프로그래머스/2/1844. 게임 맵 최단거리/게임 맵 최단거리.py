from collections import deque
def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]
    q = deque([[0,0]])
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        for j, f in [[0,1], [1,0], [0,-1], [-1,0]]:
            new_x, new_y = x+j, y+f
            if 0<=new_x< n and 0<=new_y < m and visited[new_x][new_y] == 0 and maps[new_x][new_y] == 1:
                q.append([new_x, new_y])
                visited[new_x][new_y] += visited[x][y] + 1
    if visited[n-1][m-1] != 0:
        answer = visited[n-1][m-1]
    else:
        answer = -1
    return answer