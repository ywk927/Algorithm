T = int(input())
for tc in range(1,T+1):
    N = float(input())
    i = -1
    comparison_num = 0
    ans = ''
    while i > -13:
        comparison_num += 2 ** i
        if comparison_num == N:
            ans += '1'
            break
        elif comparison_num < N:
            ans += '1'
            i -= 1
        elif comparison_num > N:
            comparison_num -= 2 ** i
            ans += '0'
            i -= 1
    if i == -13:
        print(f'#{tc} overflow')
    else:
        print(f'#{tc} {ans}')
