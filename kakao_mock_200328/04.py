'''
https://programmers.co.kr/learn/courses/30/lessons/64063
어려웠던 부분: 다음 빈방을 찾아오는 재귀함수 짜는 부분 (링크드 리스트처럼 배열을 사용했음)
효율성 풀이: 부모노드 (다음 -1을 갖고 있는 index를 품고 있는것)를 이용하는 부분 맞았으나..
배열보다는 dictionary로 푸는 것이 더 빠르고 맞았음.
'''
def solution(k, room_number):
    answer = []
    rooms = [-1]*(k+1)
    def getValue(start):            
        curr = start
        while(rooms[curr] != -1):
            curr = rooms[curr]
        rooms[curr] = curr+1
        return curr
    for num in room_number:
        val = getValue(num)
        answer.append(val)
            
    return answer


def solution_dict(k, room_number):
    answer = []
    rooms = {}
    for i in room_number:
        num = i
        visited = [num]
        while num in rooms:
            num = rooms[num]
            visited.append(num)
        answer.append(num)
        for room in visited:
            rooms[room] = num+1
    return answer


def solution2(k, room_number):
    room_dic = {}
    ret = []
    for i in room_number:
        n = i
        visit = [n]
        while n in room_dic:
            n = room_dic[n]
            visit.append(n)
        ret.append(n)
        for j in visit:
            room_dic[j] = n+1
    return ret



print(solution(10, 	[1,3,4,1,3,1]) == [1,3,4,2,5,6])