'''
151. reverse-words-in-a-string 

MEDIUM
실수원인: 함수 특성을 잘못 기억함. 
strip의 기본 separater는 white spaced이고, 여기에 " "를 넣으면 두칸짜리 이상 스페이스는 스페이스를 그대로 남김

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

'''

class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        l.reverse()
        return " ".join(l)


# FOR DEBUG
def main():
    sol = Solution()
    print(sol.reverseWords("a good   example"))
    # print(sol.reverseWords("  hello world!  "))
    # print(sol.reverseWords("a good   example"))

main()