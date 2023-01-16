def solution(x):
    num_list = []
    for i in str(x):
        num_list.append(int(i))
        harshad = sum(num_list)
    if x % harshad == 0:
        return True
    else:
        return False