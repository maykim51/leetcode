'''
MEDIUM

실수원인: deque()라는 개념, delimiter를 사용하는 개념! (잊지말자)
미리미리 큰 그림(리스트 레벨) element와, interaction을 정해놓고 쓰자. SYSTEM THINKING!
좌우 어느 방향으로 읽은 건지 bool로 판단 
'''
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        level_list = deque()
        if root is None:
            return []
        # start with the level 0 with a delimiter
        node_queue = deque([root, None])
        is_order_left = True

        while len(node_queue) > 0:
            curr_node = node_queue.popleft()

            if curr_node:
                if is_order_left:
                    level_list.append(curr_node.val)
                else:
                    level_list.appendleft(curr_node.val)

                if curr_node.left:
                    node_queue.append(curr_node.left)
                if curr_node.right:
                    node_queue.append(curr_node.right)
            else:
                # we finish one level
                ret.append(level_list)
                # add a delimiter to mark the level
                if len(node_queue) > 0:
                    node_queue.append(None)

                # prepare for the next level
                level_list = deque()
                is_order_left = not is_order_left

        return ret


def createTree(l: list) -> TreeNode:
    mapToTreeNode = {}

    for i in range(len(l)):
        if l[i] is None:
            continue

        # Create TreeNode
        if i not in mapToTreeNode:
            mapToTreeNode[i] = TreeNode(l[i])
        curr = mapToTreeNode[i]

        # Connect to children
        left = 2*i+1
        right = 2*i+2
        if left < len(l) and l[left] is not None:
            if left not in mapToTreeNode:
                mapToTreeNode[left] = TreeNode(l[left])
            curr.left = mapToTreeNode[left]
        if right < len(l) and l[right] is not None:
            if right not in mapToTreeNode:
                mapToTreeNode[right] = TreeNode(l[right])
            curr.right = mapToTreeNode[right]

    root = mapToTreeNode[0]
    return root


sol = Solution()
l = [3,9,20,None,None,15,7]
root = createTree(l)
print(sol.zigzagLevelOrder(root))