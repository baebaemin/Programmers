def solution(N, M):
    # if n > m:
    #     n, m = m, n
    n, m = min(N, M), max(N, M)

    if m % n == 0:
        return([n, m])
    
    i = 1
    while m * i % n != 0:
        i += 1
        m_num = m * i
        
    for i in range(n // 2, 0, -1):
        if m % i == 0 and n % i == 0:
            return [i, m_num]
                

print(solution(3, 12))