board_lst = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

def solution(board):
    dr = [-1, -1, -1, 0, 0, 1, 1, 1]
    dc = [-1, 0, 1, -1, 1, -1, 0, 1]
    r_point = []
    c_point = []

    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c]:  # 지뢰가 묻혀있다면
                r_point.apprnd(r)
                c_point.append(c)

    for j in range(len(r_point)):
        for i in range(8):  # 8방으로 델타 검사
            if 0 <= r_point[j] + dr[i] <= len(board) and 0 <= c_point[j] + dc[i] <= len(board):
                board[r_point[j] + dr[i]][c_point[j] + dc[i]] = 1

    cnt = 0
    for r in range(len(board)):
        for c in range(len(board)):
            if not board[r][c]:
                cnt += 1
    return cnt