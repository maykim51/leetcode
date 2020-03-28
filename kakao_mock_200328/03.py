def solution(user_id, banned_id):
    answer = 1
    sets = []
    bannedDict = {}
    for id in banned_id:
        if id not in bannedDict:
            bannedDict[id] = []
    
    def isEqual(starred, original):
        if len(original) != len(starred):
            return False
        for i in range(len(original)):
           if original[i] != starred[i] and starred[i] != '*':
               return False
        return True

    for id in bannedDict:
        for user in user_id:
            if isEqual(id, user):
                bannedDict[id].append(user)

    def pick(ans, ids, dic):
        if len(ids) == 0:
            if set(ans) not in sets:
                sets.append(set(ans))
            return
            
        curr = ids[0]
        for _ in range(len(dic[curr])):
            id = dic[curr].pop(0)
            if id not in ans:
                ans.append(id)
                pick(ans,ids[1:],dic)
                ans.pop()
            dic[curr].append(id)                        
        return
    
    pick([],banned_id, bannedDict)
    answer = len(sets)
    return answer


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"])==2)
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"])==2)
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"])==3)