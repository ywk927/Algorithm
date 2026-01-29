import heapq

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dist = [[float('inf')] * N for _ in range(N)]
    q = [(0,0,0)]
    while q:
        w, ti, tj = heapq.heappop(q)
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni, nj = ti+di, tj+dj
            if 0<=ni<N and 0<=nj<N:
                next_dist = float('inf')
                if arr[ni][nj] > arr[ti][tj]:
                    next_dist  = (arr[ni][nj] - arr[ti][tj]) * 2
                elif arr[ni][nj] == arr[ti][tj]:
                    next_dist = 1
                elif arr[ni][nj] < arr[ti][tj]:
                    next_dist = 0
                if w + next_dist < dist[ni][nj] :
                    dist[ni][nj] = w + next_dist
                    heapq.heappush(q, (dist[ni][nj], ni, nj))
    print(f'#{tc} {dist[N-1][N-1]}')