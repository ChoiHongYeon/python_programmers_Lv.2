# JadenCase 문자열 만들기 (https://school.programmers.co.kr/learn/courses/30/lessons/12951?language=python3)

def solution(s):

    answer = s[0].upper()
    for i in range(1, len(s)):
        if s[i - 1] == " ":
            answer += s[i].upper()
        else:
            answer += s[i].lower()

    return answer

print(solution("3people unFollowed me"))
print(solution("for the last week"))