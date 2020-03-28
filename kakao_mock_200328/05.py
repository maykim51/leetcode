def solution(stones, k):
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



print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3) == 3)
