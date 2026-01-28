T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            candidate = 0
            ti, tj = i, j
            candidate += arr[ti][tj]
            for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                for k in range(1,M):
                    ni, nj = ti+di*k, tj+dj*k
                    if 0<=ni<N and 0<=nj<N:
                        candidate += arr[ni][nj]
            if ans < candidate:
                ans = candidate
            candidate = arr[ti][tj]
            for fi, fj in [[-1,-1], [1,1], [-1,1], [1,-1]]:
                for k in range(1,M):
                    ni, nj = ti+ fi*k, tj + fj*k
                    if 0<=ni<N and 0<=nj<N:
                        candidate += arr[ni][nj]
            if ans < candidate:
                ans = candidate
    print(f'#{tc} {ans}')