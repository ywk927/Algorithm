# def solution(m, n, h, w, drops):
#     answer = [0,0]
#     arr = [[0] * n for _ in range(m)]
#     i = 1
#     for drop in drops:
#         arr[drop[0]][drop[1]] = i
#         i += 1
#     got_answer = False
#     answer_candidate = 0
#     for i in range(m-h+1):
#         if got_answer:
#             break
#         for j in range(n-w+1):
#             cnt = 0
#             rain_number = m*n
#             for k in range(i, i+h):
#                 for l in range(j, j+w):
#                     if arr[k][l] == 0:
#                         cnt += 1
#                     else:
#                         if rain_number > arr[k][l]:
#                             rain_number = arr[k][l]
#             if cnt == h*w:
#                 answer[0] = i
#                 answer[1] = j
#                 got_answer = True
#                 break
#             else:
#                 if rain_number > answer_candidate:
#                     answer[0] = i
#                     answer[1] = j
#                     answer_candidate = rain_number
#     return answer
from collections import deque

def solution(m, n, h, w, drops):
    answer = [0, 0]
    INF = len(drops) + 1

    # 1. 비 내린 순서 기록 (안 내린 칸은 INF)
    arr = [[INF] * n for _ in range(m)]
    i = 1
    for r, c in drops:
        arr[r][c] = i
        i += 1

    # 2. 각 행에서 너비 w 구간의 최소값 구하기
    # row_min[i][j] = arr[i][j:j+w]의 최소값
    row_min = [[0] * (n - w + 1) for _ in range(m)]

    for i in range(m):
        dq = deque()
        for j in range(n):
            while dq and arr[i][dq[-1]] >= arr[i][j]:
                dq.pop()
            dq.append(j)

            # 윈도우 범위 벗어난 인덱스 제거
            if dq[0] <= j - w:
                dq.popleft()

            # 길이 w 윈도우가 만들어졌으면 최소값 기록
            if j >= w - 1:
                row_min[i][j - w + 1] = arr[i][dq[0]]

    # 3. 각 열에서 높이 h 구간의 최소값 구하기
    # 즉 h x w 직사각형 전체의 최소값
    answer_candidate = -1

    for j in range(n - w + 1):
        dq = deque()
        for i in range(m):
            while dq and row_min[dq[-1]][j] >= row_min[i][j]:
                dq.pop()
            dq.append(i)

            # 윈도우 범위 벗어난 인덱스 제거
            if dq[0] <= i - h:
                dq.popleft()

            # 높이 h 윈도우가 만들어졌으면 직사각형 최소값 확인
            if i >= h - 1:
                rain_number = row_min[dq[0]][j]
                top_row = i - h + 1

                if rain_number > answer_candidate:
                    answer_candidate = rain_number
                    answer[0] = top_row
                    answer[1] = j

    return answer