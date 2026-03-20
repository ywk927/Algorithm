# def solution(land):
#     c = len(land[0])
#     r = len(land)
#     answer = 0
#     for sichu in range(c):
#         candidate = 0
#         land_cnt = [[0] * c for _ in range(r)]
#         for i in range(r):
#             if land[i][sichu] == 1 and land_cnt[i][sichu] == 0:
#                 q = [(i,sichu)]
#                 land_cnt[i][sichu] = 1
#                 while q:
#                     x, y = q.pop()
#                     candidate += 1
#                     for di, dj in [[0,1], [1,0], [-1,0], [0,-1]]:
#                         ti, tj = x+di, y+dj
#                         if 0<= ti < r and 0<= tj < c and land_cnt[ti][tj] == 0 and land[ti][tj] == 1:
#                             land_cnt[ti][tj] = 1
#                             q.append((ti,tj))
#         print(candidate)
#         if answer < candidate:
#             answer = candidate
#     return answer
def solution(land):
    c = len(land[0])
    r = len(land)
    land_cnt = [[0] * c for _ in range(r)]
    answer = 0
    candidates = [0 for _ in range(c)]
    for i in range(r):
        for j in range(c):
            if land[i][j] == 1 and land_cnt[i][j] == 0:
                q = [(i,j)]
                land_cnt[i][j] = 1
                legit_column = []
                cnt = 0
                while q:
                    ti, tj = q.pop()
                    if tj not in legit_column:
                        legit_column.append(tj)
                    cnt += 1
                    for di, dj in [[0,1], [1,0], [-1,0], [0,-1]]:
                        ni, nj = ti+di, tj+dj
                        if 0<= ni < r and 0<= nj < c and land_cnt[ni][nj] == 0 and land[ni][nj] == 1:
                            land_cnt[ni][nj] = 1
                            q.append((ni,nj))
                for col in legit_column:
                    candidates[col] += cnt
    for i in candidates:
        if i > answer:
            answer = i
    return answer