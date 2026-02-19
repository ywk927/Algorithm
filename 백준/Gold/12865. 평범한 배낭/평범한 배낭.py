N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]
# 1차원 배열로 받아서 생각해보자
# 최대 부피는 K 이므로 그 만큼을 기록할 수 있는 배열을 생성하자
dp = [0] * (K + 1)
# 저장해놓은 각 아이템의 부피와 가치를 꺼내와서 비교
for v, c in items:
    # w-v가 -1로 넘어가지 않게 range 조정, 즉 해당 item의 v를 쓰면 최대 부피인 K를 넘어가는 일이 없다
    for w in range(K, v - 1, -1):
        # 계속 max 값을 전에 활용한 값과 비교하여 업데이트한다
        dp[w] = max(dp[w], dp[w - v] + c)
print(dp[K])