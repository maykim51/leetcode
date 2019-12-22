'''
Leetocde # 20
https://leetcode.com/problems/valid-parentheses/
Easy

실수
- 경우 나누기
- 잘못된 입력 (s가 잘못된 경우)

큰 움직임부터 설계해서, 변수에 저장하고 수행하기. (end element와 비교한다 -> end element를 정의를 먼저 한다.)
recurring으로 풀어볼 수 있을까?
'''

class Solution:
    mapping = {")":"(", "]":"[", "}":"{"}
    

    def isValid(self, s: str) -> bool:
        if s is "":
            return True

        stack = []                
        for char in s:
            #if it's closing,
            if char in self.mapping:
                top_element = stack.pop() if stack else "#"
                if self.mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        
        
        return not stack


sol = Solution()
print(sol.isValid("()"))