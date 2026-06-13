def solution(want, number, discount):
    answer = 0
    m = len(want)
    real_want = []
    for i in range(m):
        for _ in range(number[i]):
            real_want.append(want[i])
    real_want.sort()
    n = len(discount)
    index = 0
    while index <= n-10:
        expected_discount = []
        for i in range(index, index+10):
            expected_discount.append(discount[i])
        expected_discount.sort()
        if real_want == expected_discount:
            answer += 1
        index += 1
    return answer