# 모음사전 (https://school.programmers.co.kr/learn/courses/30/lessons/84512?language=python3)

def solution(word):

    kinds = ["A", "E", "I", "O", "U"]
    now_word = ["", "", "", "", ""]
    target_word = list(word)
    for i in range(0, 5 - len(target_word)):
        target_word.append("")
    answer = 0

    while True:

        answer += 1

        if now_word[4] == "":
            for i in range(0, 5):
                if now_word[i] == "":
                    now_word[i] = "A"
                    break
        elif now_word[4] == "U":
            tmp = 4
            while True:
                if now_word[tmp] == "U":
                    now_word[tmp] = ""
                    tmp -= 1
                else:
                    break
            now_word[tmp] = kinds[kinds.index(now_word[tmp]) + 1]
        else:
            now_word[4] = kinds[kinds.index(now_word[4]) + 1]

        if now_word == target_word:
            break

    return answer

print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))