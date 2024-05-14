# 요격 시스템 (https://school.programmers.co.kr/learn/courses/30/lessons/181188?language=python3)

def solution(targets):
    
    targets.sort()
    i = 0
    while i + 1 < len(targets):
        if targets[i][0] == targets[i + 1][0]:
            del targets[i + 1]
        else:
            i += 1

    i = 0
    while i + 1 < len(targets):
        if targets[i][1] > targets[i + 1][0]:
            del targets[i + 1]
        else:
            i += 1

    return len(targets)

result = solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]])
print(result)