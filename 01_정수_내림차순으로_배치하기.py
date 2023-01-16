def solution(n):
    num_list = []
    for i in str(n):
        num_list.append(i)
    rev = sorted(num_list)[::-1]
    return int(''.join(str(s) for s in rev))
    