def solution(n, m):
    if n > m:
        n, m = m, n
    elif m % n == 0:
        return([n, m])
    else:
        for i in range(n // 2, 0, -1):
            if m % i == 0 and n % i == 0:
                return([i, (m // i) * (i ** 2)])
                

print(solution(24, 248))