# 숫자 변환하기 (https://school.programmers.co.kr/learn/courses/30/lessons/154538)

def solution(x, y, n):
    
    answer = 0
    OX = ["O", "O", "O"]

    while y > x and "O" in OX:
        add_n = y
        mul_2 = y
        mul_3 = y

        if OX[0] == "O":
            if add_n >= x:
                add_n = y - n

        if OX[1] == "O":
            if y % 2 == 0 and y / 2 >= x:
                mul_2 = y / 2
            else:
                OX[1] = "X"

        if OX[2] == "O":
            if y % 3 == 0 and y / 3 >= x:
                mul_3 = y / 3
            else:
                OX[2] = "X"

        y = min(add_n, mul_2, mul_3)
        answer += 1

    if x != y:
        answer = -1

    return answer

result1 = solution(10, 40, 5)
result2 = solution(10, 40, 30)
result3 = solution(2, 5, 4)

print(result1, result2, result3)