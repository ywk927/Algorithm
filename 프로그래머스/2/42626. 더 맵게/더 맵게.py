import heapq
def solution(scoville, K):
    answer = 0
    arr = []
    for num in scoville:
        heapq.heappush(arr, num)
    while True:
        if arr[0] >= K:
            break
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)
        heapq.heappush(arr, a + 2 * b)
        answer += 1
        if len(arr) == 1 and arr[0] < K:
            answer = -1
            break
        if arr[0] >= K:
            break
    return answer