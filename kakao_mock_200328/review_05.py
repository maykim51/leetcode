'''
https://tech.kakao.com/2020/04/01/2019-internship-test/
https://programmers.co.kr/learn/courses/30/lessons/64062

나의 풀이: 답은 맞췄는데 효율성은 틀림!
-> 000이 연속으로 나오는 구간을 찾는다 > 합이 가장 작은 연속된 구간을 찾는다!

실수한 부분: 마지막 edge case를 잘 이해못하겠음. 왜 l<r 이 아니고 l<r-1 이고 마지막에 r은 건널 수 있는지는 왜 체크 하는 걸까?


효율성 풀이: 이분탐색으로 찾기!
건널수 있다? -> 다음 범위는 M ~ MAX
건널 수 없다 -> 다음 범위는 lo ~ M-1

'''
# O(N) 풀이 연속된 000위치를 찾는다. 답은 맞는데 효율성은 틀리다.
def solution2(stones, k):
    answer = 0
    mn = min(stones)
    mnIdx = []

    def findMinSum(i):
        minSum = float("INF")
        resStart = -1
        start = i-(k-1)
        for _ in range(k):
            if start >= 0 and start+k-1 < len(stones):
                sm = sum(stones[start:start+k])
                if sm < minSum:
                    minSum = sm
                    resStart = start
                elif sm == minSum:
                    if max(stones[start:start+k]) > max(stones[resStart:resStart+k]):
                        minSum = sm
                        resStart = start
            start += 1
        return (sum(stones[resStart:resStart+k]),resStart, resStart+k-1)

    for i in range(len(stones)):
        if stones[i] == mn:
            mnIdx.append(i)

    mnSum, start, end = float("INF"), -1, -1
    for i in mnIdx:
        cMnSum, cStart, cEnd = findMinSum(i)
        if cMnSum < mnSum:
            mnSum, start, end = cMnSum, cStart, cEnd
        elif cMnSum == mnSum and max(stones[cStart:cEnd+1]) > max(stones[start:end+1]):
            mnSum, start, end=cMnSum, cStart, cEnd
    
    answer=max(stones[start:end+1])

    return answer


####################### O(nlogm) 풀이 (n: 징검다리 갯수 m: 최댓값)
def check(stones,k,n):
    temp = k
    for stone in stones:
        if stone < n:
            temp -= 1
        else:
            temp = k

        if temp == 0:
            return False
    return True

def solution(stones, k):
    l = 0
    r = 200000000
    while l<r-1:
        n = (l+r)//2
        canJump = check(stones,k,n)

        if canJump:
            l = n
        else:
            r = n

    rok = check(stones,k,r)
    if rok:
        return r
    else:
        return l




print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3) == 3)
