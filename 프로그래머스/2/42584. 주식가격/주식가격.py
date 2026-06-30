# def solution(prices):
#     answer = []
#     # 떨어지지 않은 기간을 기록
#     # 가장 낮을 가격을 업데이트 하면서 인덱스와 같이 업데이트 -> x
#     n = len(prices)
#     for i in range(n):
#         standard = prices[i]
#         cnt = 0
#         for j in range(i+1, n):
#             if standard <= prices[j]:
#                 cnt += 1
#                 if j == n-1:
#                     answer.append(cnt)
#                     # print(i,j)
#             elif standard > prices[j]:
#                 cnt += 1
#                 answer.append(cnt)
#                 # print(i,j)
#                 break
#     answer.append(0)
    
#     return answer

def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []

    for i in range(n):

        # 현재 가격이 더 작다면
        while stack and prices[stack[-1]] > prices[i]:
            idx = stack.pop()
            answer[idx] = i - idx

        stack.append(i)

    # 끝까지 가격이 떨어지지 않은 경우
    while stack:
        idx = stack.pop()
        answer[idx] = n - 1 - idx

    return answer