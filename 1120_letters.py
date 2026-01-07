A, B = input().split()
N, M = len(A), len(B)
ans = 10 ** 10
for i in range(M-N+1):
    diff = 0
    for j in range(N):
        if A[j] != B[i + j]:
            diff += 1
    ans = min(ans, diff)
print(ans)