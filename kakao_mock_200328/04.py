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


print(solution(10, 	[1,3,4,1,3,1]) == [1,3,4,2,5,6])