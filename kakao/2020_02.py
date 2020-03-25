'''
잘 풀었고, 맞췄음. 단 시간이 좀 오래 걸렸음.
'''
def solution(p):
    answer = ''
    if p == '':
        return ''
    def isRight(c):
        cnt = 0
        for i in range(len(c)):
            cnt = cnt + 1 if c[i] == '(' else cnt - 1
            if cnt < 0: return False
        return True

    def isBalanced(s): return s.count('(') == s.count(')')

    if isRight(p):
        return p

    u, v = "",""
    for i in range(1,len(p),2):
        if isBalanced(p[:i+1]):
            u, v = p[:i+1], p[i+1:]
            break

    if isRight(u):
        answer += u + solution(v)
    else:
        answer = "(" + solution(v) + ")"
        if len(u) >= 2:
            answer += u[1:-1].replace('(','0').replace(')','(').replace('0',')')

    return answer

# print(solution("(()())()")=="(()())()")
print(solution(")(")=="()")
print(solution("()))((()") == "()(())()")