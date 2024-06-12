# 혼자서 하는 틱택토 (https://school.programmers.co.kr/learn/courses/30/lessons/160585?language=python3)

def solution(board):

    B=[]
    O_count = 0
    X_count = 0
    for i in range(3):
        B.append(list(board[i]))
        O_count += B[i].count('O')
        X_count += B[i].count('X')
    B_count = O_count + X_count

    OX = ['O', 'X']
    OX_bingo = [0, 0]
    for i in range(2):
        for j in range(3):
            if OX[i] * 3 == B[j][0] + B[j][1] + B[j][2]:
                OX_bingo[i] += 1
            if OX[i] * 3 == B[0][j] + B[1][j] + B[2][j]:
                OX_bingo[i] += 1
        if OX[i] * 3 == B[0][0] + B[1][1] + B[2][2]:
            OX_bingo[i] += 1
        if OX[i] * 3 == B[0][2] + B[1][1] + B[2][0]:
            OX_bingo[i] += 1

    answer = 0
    if B_count == 0 or B_count == 2 or B_count == 4:
        if O_count == X_count:
            answer = 1
    elif B_count == 1 or B_count == 3 or B_count == 5:
        if O_count == X_count + 1:
            answer = 1
    elif B_count == 6 or B_count == 8:
        if O_count == X_count and OX_bingo[0] == 0:
            answer = 1
    elif B_count == 7 or B_count == 9:
        if O_count == X_count + 1 and OX_bingo[1] == 0:
            answer = 1

    return answer

result1 = solution(["O.X", ".O.", "..X"])
result2 = solution(["OOO", "...", "XXX"])
result3 = solution(["...", ".X.", "..."])
result4 = solution(["...", "...", "..."])

print(result1, result2, result3, result4)