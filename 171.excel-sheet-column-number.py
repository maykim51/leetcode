'''
Leetcode 171.
Easy
https://leetcode.com/problems/excel-sheet-column-number/discuss/52304/Python-concise-solution.
A - 1
B- 2
C - 3
 Z -> 26
AA -> 27
AB -> 28 
'''

def col_to_num(s):
    res = 0
    s = s.upper()
    for i in s:
        res = res*26 + ord(i)-ord('A') +1
    return res

print(col_to_num('a'))
print(col_to_num('Z'))
print(col_to_num('AA'))
print(col_to_num('AB'))