"""
20.03.11

1. 기존 노드 : 신규 노드 형태의 딕셔너리를 만들어서 제작. 새로운 노드를 만났을 때만 deep copy 하는 방법. O(N)
2. 사이사이에 끼워넣어서 weave 하기 (next, random 등..) (O(N) space만 O(1))

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
#FOR DEBUG
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def __init__(self):
        self.visitedHash = {}

    # recursively returns newly created Node.
    def copyRandomList(self, head: 'Node') -> 'Node':
        # Base case
        if head == None:
            return None
        if head in self.visitedHash:
            return self.visitedHash[head]

        node = Node(head.val, None, None)
        self.visitedHash[head] = node

        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node


# FOR DEBUG
    # def printLinkedList(self, start: 'Node'):
    #     res = "["
    #     currentNode = start
    #     while(currentNode is not None):
    #         node = "["+str(currentNode.val)+","+str(currentNode.random)+"]"
    #         if self.isTail(currentNode) is False:
    #             node+=","
    #         res += node
    #         currentNode = currentNode.next
    #     res += "]"
    #     print(res)
    
    # def isTail(self, node: 'Node'):
    #     if node.next is None:
    #         return True
    #     return False
        


def main():
    sol = Solution()
    head = Node(7, None,None)
    head.next = Node(13,None ,0)
    head.next.next = Node(11,None,4)
    head.next.next.next = Node(10,None,2)
    head.next.next.next.next = Node(1,None,0)
    sol.copyRandomList(head)
    

main()