from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    # 엣지 케이스 때문에 2배로 확장해서 풀기...
    arr = [[0] * 102 for _ in range(102)]
    visited = [[0] * 102 for _ in range(102)]
    min_width, min_height = 102, 102
    max_width, max_height = 0, 0
    for each in rectangle:
        # x 가 열 = 가로, y가 행 = 세로
        start_x, start_y = each[0] * 2, each[1] * 2
        end_x, end_y = each[2] * 2, each[3] * 2
        if start_y < min_height:
            min_height = start_y
        if start_x < min_width:
            min_width = start_x
        if end_y > max_height:
            max_height = end_y
        if end_x > max_width:
            max_width = end_x
        for y in range(start_y, end_y + 1):
            for x in range(start_x, end_x + 1):
                arr[100-y][x] = 1
    start_width = min_width
    end_width = max_width
    start_height = 100 - max_height
    end_height = 100 - min_height
    # print(start_width, start_height, end_width, end_height) # 1, 41, 8 ,49 -> 2, 82, 16, 98
    # print(arr)
    # 8 방향 탐색하기? -> 비효율적... range를 주자
    direction = [(-1,0), (0,-1), (1,0), (0,1), (1,1), (-1, -1), (1,-1), (-1,1)]
    for i in range(start_height, end_height + 1):
        for j in range(start_width, end_width + 1):
            for di, dj in direction:
                if arr[i][j] == 1 and arr[i+di][j+dj] == 0:
                    arr[i][j] = 2
                    break
    # print(arr)
    # 이제 bfs 시작
    directions = [(0,1), (1,0), (-1,0), (0,-1)]
    q = deque([])
    q.append((100 - characterY * 2, characterX * 2))
    visited[100 - characterY * 2][characterX * 2] = 1
    while q:
        ti, tj = q.popleft()
        if ti == 100 - itemY * 2 and tj == itemX * 2:
            break
        for di, dj in directions:
            ni, nj = ti+di, tj + dj
            if 0<=ni<102 and 0<=nj<102 and visited[ni][nj] == 0 and arr[ni][nj] == 2:
                visited[ni][nj]  = visited[ti][tj] + 1
                q.append((ni,nj))
    answer = (visited[100 - itemY * 2][itemX * 2] - 1 ) // 2
    return answer