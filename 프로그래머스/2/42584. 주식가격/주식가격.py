def solution(prices):
    answer = []
    # 떨어지지 않은 기간을 기록
    # 가장 낮을 가격을 업데이트 하면서 인덱스와 같이 업데이트 -> x
    n = len(prices)
    for i in range(n):
        standard = prices[i]
        cnt = 0
        for j in range(i+1, n):
            if standard <= prices[j]:
                cnt += 1
                if j == n-1:
                    answer.append(cnt)
                    # print(i,j)
            elif standard > prices[j]:
                cnt += 1
                answer.append(cnt)
                # print(i,j)
                break
    answer.append(0)
    
    return answer