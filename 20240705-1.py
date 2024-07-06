# 뒤에 있는 큰 수 찾기 (https://school.programmers.co.kr/learn/courses/30/lessons/154539)

def solution(numbers):

    answer = [-1] * len(numbers)
    stack = []
    
    for i in range(len(numbers) - 1, -1, -1):
        while len(stack) > 0 and stack[-1] <= numbers[i]:
            stack.pop()
        if len(stack) > 0:
            answer[i] = stack[-1]
        stack.append(numbers[i])
    
    return answer

result1 = solution([2, 3, 3, 5])
result2 = solution([9, 1, 5, 3, 6, 2])

print(result1)
print(result2)