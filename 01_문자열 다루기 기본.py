def solution(s):
    if len(s) == 4 or len(s) == 6:
        for i in s:
            if ord(f'{i}') > 57:
                return False
        else: return True
    return False

#다른 사람의 풀이
#def alpha_string46(s):
#    return s.isdigit() and len(s) in (4, 6)
