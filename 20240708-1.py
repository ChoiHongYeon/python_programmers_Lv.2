# 숫자 변환하기 (https://school.programmers.co.kr/learn/courses/30/lessons/154538)

def solution(x, y, n):

    answer = 0

    while y > x:

        add_n = y
        mul_2 = y
        mul_3 = y

        if y - n >= x:
            add_n = y - n
        if y % 2 == 0 and y // 2 >= x:
            mul_2 = y // 2
        if y % 3 == 0 and y // 3 >= x:
            mul_3 = y // 3

        next_y = min(add_n, mul_2, mul_3)
        if next_y == y:
            answer = -1
            break
        y = next_y
        answer += 1

    return answer

result1 = solution(10, 40, 5)
result2 = solution(10, 40, 30)
result3 = solution(2, 5, 4)

print(result1, result2, result3)