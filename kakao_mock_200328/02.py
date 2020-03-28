'''
slice 전처리 필요 {}
길이순으로 나열한 후 m.sort(key=len)
answer []에 여집합만 추가
'''
def solution(s):
    answer = []
    partialSets = s[2:-2].split('},{')

    for i in range(len(partialSets)):
        numbs = partialSets[i].split(',')  
        partialSets[i] = set(list(map(int,numbs)))
    partialSets.sort(key=len)

    for el in partialSets:
        answer.extend(el - set(answer))

    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}") == [2, 1, 3, 4])
print(solution("{{123}}") == [123])
print(solution(	"{{20,111},{111}}")==[111, 20])