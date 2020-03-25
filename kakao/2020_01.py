'''
kakao blind 2020 1번문제 - 맞췄음!
https://programmers.co.kr/learn/courses/30/lessons/60057?language=python3
'''
def solution(s):
    N = len(s)
    answer = 0
    mn = N

    for size in range(1, N//2+1):
        #heuristic
        if size > mn-1:
            continue

        copy = ""
        curr = 0
        while(curr < N):
            if s[curr:curr+size] != s[curr+size:curr+size+size]:
                copy += s[curr:curr+size]
                curr += size
                continue
            else:
                cnt = 2
                word = s[curr:curr+size]
                curr += size
                while(s[curr:curr+size] == s[curr+size:curr+size+size]):
                    cnt += 1
                    curr += size
                copy += str(cnt)+word
                curr += size

        mn = min(mn, len(copy))
                
    answer = mn
    return answer

print(solution("aabbaccc") == 7)
print(solution("ababcdcdababcdcd") == 9)
print(solution("abcabcdede") == 8)
print(solution("abcabcabcabcdededededede") == 14)
print(solution("xababcdcdababcdcd") == 17)
