def solution(n):
    str_n = str(n)
    num_list = []
    for i in str_n:
        num_list.append(int(i))
        
    return sum(num_list)