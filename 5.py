'''
Leetcdode # longest

Amazon top #5

#실수
case 나누기 -> 스스로 palindrome 인 경우

# 다른 방법 (그래도 지금 풀이가 더 나음)
reverse 한다음에 longest sub string 찾고, palindrome 인지 확인하는 방법
완전탐색 외에 DP, String manipulation도 시도해 볼 수 있었음.

# 더 나은 방법 - Manacher's algorithm
'''
class Solution():
    def longestPalindrome(self,s:str)->str:
        if not s:
            return ""

        s = "#".join(list(s))
        
        palindrome = ""
        for i in range(1, len(s)-1):
            left, right = -1, -1
            if i%2 == 0 and s[i-2] == s[i+2]:
                left, right = i-2, i+2                
            elif i%2 == 1 and s[i-1] == s[i+1]:
                left, right = i-1, i+1
            
            if left != -1 and right != -1:
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    left -= 2
                    right += 2
                left += 2
                right -= 2
                new_str = s[left:right+1].replace("#","")
                if len(new_str) > len(palindrome):
                    palindrome = new_str
        if palindrome == "":
            return s[0]
        return palindrome


sol = Solution()
print(sol.longestPalindrome("babad"))
print(sol.longestPalindrome("cbbd"))