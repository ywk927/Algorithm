def solution(n):
    # n = 4인 경우 첫 행의 기준으로 4개의 열에서 대해서 체크만 해준다. 기록은 queen 되는 자리 기준으로 기록한다. 이게 n개에 도달하면 answer += 1 하기
    def check(r,c):
        # 위에 열 체크
        for i in range(r):
            if arr[i][c] == 1:
                return False
        # 왼쪽 위 대각선 체크 (\)
        i, j = r-1, c-1
        while i>=0 and j>=0:
            if arr[i][j] == 1:
                return False
            i -= 1
            j -= 1
        # 오른쪽 위 대각선 체크 (/):
        k,l = r-1, c+1
        while k>=0 and l<n:
            if arr[k][l] == 1:
                return False
            k -= 1
            l += 1
        return True
        # directions = [(-1,0), (-1,-1), ((-1,1))] # 위, 아래, 오, 왼, 대각4방향
        # for di, dj in directions:
        #     for k in range(1,f+1):
        #         ni, nj = ti + di*k, tj + dj*k
        #         if 0<=ni<n and 0<=nj<n and arr[ni][nj] == 1:
        #             return False
        # return True
    
    def backtrack(i):
        nonlocal answer
        if i == n:
            answer += 1
            return
        else:
            for j in range(n):
                if check(i,j):
                    arr[i][j] = 1 # 거기에 퀸을 두고 다음 행을 탐색한다
                    backtrack(i+1)
                    arr[i][j] = 0 # 만약 막혔으면 나와서 그 자리를 방문안한것으로 기록하고 다음 열을 탐색하도록
    arr = [[0] * n for _ in range(n)]
    answer = 0
    backtrack(0)
    return answer