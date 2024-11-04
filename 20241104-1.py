# 할인 행사 (https://school.programmers.co.kr/learn/courses/30/lessons/131127?language=python3)

def solution(want, number, discount):

    answer = 0

    for i in range(0, len(discount) - 9):
        if discount[i] in want:
            tenDays = discount[i : i + 10]
            signUp = True
            for j in range(len(want)):
                if tenDays.count(want[j]) != number[j]:
                    signUp = False
                    break
            if signUp == True:
                answer += 1

    return answer

print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
print(solution(["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))