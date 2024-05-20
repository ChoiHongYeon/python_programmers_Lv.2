# 두 원 사이의 정수 쌍

import math

def solution(a, b):
    
    a2 = a ** 2
    b2 = b ** 2

    z = ((b - a) + 1) * 4 # xy좌표 하나라도 0인 경우

    s = (int(math.sqrt((b ** 2) / 2)) - (int(math.sqrt((a ** 2) / 2) + 1)) + 1) * 4 # xy좌표 같은 경우

    o = 0
    for i in range(1, b):
        for j in range(1, int(math.sqrt((b ** 2) / 2)) + 1):
            if i > j and (i ** 2) + (j ** 2) >= a2 and (i ** 2) + (j ** 2) <= b2:
                o += 1
    o *= 8 # 그 외의 경우
    
    answer = z + s + o
    return answer

result = solution(2,3)
print(result)