'''
잘 풀었는데 Null 처리가 안됐음.
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root.val is None or root is None:
            return 0

        paths = 0
        possibleSumLists = {}
        
        def possibleSumList(root) -> list:
            if root in possibleSumLists:
                print(possibleSumLists.keys())
                return possibleSumLists[root]
            
            ret = [root.val]
            if root.left:
                for each in possibleSumList(root.left):
                    if root.val == None:
                        ret.append(0 + each)
                    else:
                        ret.append(root.val + each)
            if root.right:
                for each in possibleSumList(root.right):
                    if root.val == None:
                        ret.append(0 + each)
                    else:
                        ret.append(root.val + each)
            possibleSumLists[root] = ret
            return ret
        
        paths += possibleSumList(root).count(sum)
        return paths + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)



def createTree(l):
    mapToTreeNode = {}

    for i in range(len(l)):
        # Create TreeNode
        if i not in mapToTreeNode:
            mapToTreeNode[i] = TreeNode(l[i])
        curr = mapToTreeNode[i]

        # Connect to children
        left = 2*i+1
        right = 2*i-1
        if left < len(l):
            if left not in mapToTreeNode:
                mapToTreeNode[left] = TreeNode(l[left])
            curr.left = mapToTreeNode[left]
        if right < len(l):
            if right not in mapToTreeNode:
                mapToTreeNode[right] = TreeNode(l[right])
            curr.right = mapToTreeNode[right]

    return mapToTreeNode[0]



sol = Solution()
root = createTree([10,5,-3,3,2,None,11,3,-2,None,1])
print(sol.pathSum(root,0))