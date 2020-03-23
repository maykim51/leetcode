'''
EASY

USE SLICE, and pop, pop(0) -> [::1] and [::-1]

'''
class Solution:
    def spiralOrder(self, matrix):
        res = []
        while matrix:
            res.extend(matrix.pop(0)) #row left to right
            if matrix and matrix[0]: #top to down
                for row in matrix:
                    res.append(row.pop())
            if matrix:
                res.extend(matrix.pop()[::-1]) #row right to left
            if matrix and matrix[0]: #down to top
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        return res

sol = Solution()
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(sol.spiralOrder(matrix))