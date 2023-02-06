board_lst = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0]]
# 16


def solution(board):
    # find index of 1 -> board[i][j]
    dr = [-1, -1, -1, 0, 0, 1, 1, 1]
    dc = [-1, 0, 1, -1, 1, -1, 0, -1]

    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c]:  # 지뢰가 묻혀있다면
                break

    for i in range(8):  # 8방으로 델타 검사
        print(i, r + dr[i], c + dc[i]) ##
        if 0 <= r + dr[i] <= len(board) and 0 <= c + dc[i] <= len(board):
            board[r + dr[i]][c + dc[i]] = 1

    print(board)

    cnt = 0
    for r in range(len(board)):
        for c in range(len(board)):
            if not board[r][c]:
                cnt += 1
    return cnt

print(solution(board_lst))