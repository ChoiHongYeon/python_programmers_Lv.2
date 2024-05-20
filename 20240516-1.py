# 두 원 사이의 정수 쌍

import math

def solution(a, b):
    
    a2 = a ** 2
    b2 = b ** 2

    z = ((b - a) + 1) * 4 # xy좌표 하나라도 0인 경우

    s = (int(math.sqrt((b ** 2) / 2)) - (int(math.sqrt((a ** 2) / 2) + 1)) + 1) * 4 # xy좌표 같은 경우

    o = 0
    for x in range(1, int(math.sqrt((b ** 2) / 2)) + 1):
        min_y = 0
        max_y = 0
        if x < a:
            min_y = math.ceil(math.sqrt((a ** 2) - (x ** 2)))
            if min_y <= x:
                min_y = x + 1
            max_y = int(math.sqrt((b ** 2) - (x ** 2)))
        else:
            if x + 1 <= math.sqrt((b ** 2) - (x ** 2)):
                min_y = x + 1
            max_y = int(math.sqrt((b ** 2) - (x ** 2)))
        if min_y != 0 and max_y >= min_y:
            o += (max_y - min_y + 1)
    o *= 8 # 그 외의 경우
    
    answer = z + s + o
    return answer

result = solution(2,3)
print(result)