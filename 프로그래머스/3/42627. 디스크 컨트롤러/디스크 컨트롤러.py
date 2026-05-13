import heapq
def solution(jobs):
    n = len(jobs)
    arr = []
    answer = 0
    current_time = 0
    work_num = 1
    for lists in jobs:
        heapq.heappush(arr, [lists[1], lists[0], work_num])
        work_num += 1
    while arr:
        temp = []
        is_selected = False
        while arr:
            a = heapq.heappop(arr)
            if a[1] <= current_time:
                current_time += a[0]
                answer += (current_time - a[1])
                is_selected = True
                break
            else:
                temp.append(a)       
        for value in temp:
            heapq.heappush(arr, value)
        if is_selected == False:
            current_time = min(job[1] for job in arr)
    return answer // n