def solution(s):
    line = s.lower()
    chr_list = []
    for i in line:
        chr_list.append(i)
    num_p = chr_list.count('p')
    num_y = chr_list.count('y')
    if num_p != num_y:
        return False
    else:
        return True