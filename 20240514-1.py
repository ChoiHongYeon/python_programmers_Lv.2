# 요격 시스템 (https://school.programmers.co.kr/learn/courses/30/lessons/181188?language=python3)

def solution(targets):
    
    sorted_targets = sorted(targets, key = lambda x : x[1])
    answer = 0
    number = 0
    
    for i in range(len(targets)):
        if number <= sorted_targets[i][0]:
            answer += 1
            number = sorted_targets[i][1]

    return answer

result = solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]])
print(result)