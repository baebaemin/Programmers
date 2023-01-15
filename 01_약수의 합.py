def solution(n):
    num = int(n)
    num_list = []
    for a in range(1, int(num/2)+1): 
        if num % a == 0:
            b = num // a
            if a * b == num:
                num_list.append(b)
    num_list.append(1)
    if n == 0:
        num_list = [0]
    return sum(num_list)