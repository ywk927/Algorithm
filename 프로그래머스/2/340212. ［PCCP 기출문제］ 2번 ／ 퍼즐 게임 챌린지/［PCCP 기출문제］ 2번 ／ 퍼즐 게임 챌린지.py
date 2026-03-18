def solution(diffs, times, limit):
    n = len(diffs)
    max_diff = 0
    for i in range(n):
        max_diff = max(diffs[i], max_diff)
    left, right = 1, max_diff
    answer = max_diff
    while left <= right:
        time_taken = 0
        level = (left + right) // 2
        cnt = 0
        for i in range(n):
            if time_taken > limit:
                break
            level_diff = level - diffs[i]
            if level_diff >= 0 :
                time_taken += times[i]
            else:
                time_taken += (times[i] + times[i-1]) * abs(level_diff) + times[i]
            cnt += 1
        if cnt == n and time_taken <= limit:
            answer = level
            right = level - 1
        else:
            left  = level + 1
    return answer