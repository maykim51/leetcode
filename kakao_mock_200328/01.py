def solution(board, moves):
    answer = 0
    if not moves:
        return answer
    
    N = len(board)
    stack = []
    moves = list(map(lambda x: x-1, moves))
    
    
    def setTop(board):
        tops = [-1]*N
        for c in range(N):
            for r in range(N):
                if board[r][c] != 0 and tops[c] == -1:
                    tops[c] = r
                    break
        return tops
    

    tops = setTop(board)

    for col in moves:
        if tops[col] < N:
            curr = board[tops[col]][col]
            if len(stack) > 0 and stack[-1] == curr:
                answer += 2
                stack.pop()
            else:
                stack.append(curr)
            tops[col] += 1

    return answer



board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board,moves) == 4)