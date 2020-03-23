# -*- coding: utf-8 -*-
'''
Leetcode# 1. Easy
Amazon Frequency #1

풀이방법을 비교해보고 시작했어야 함. 예상보다 완전탐색보다 해시맵이 더 빠르다!

range edge 정리를 틀렸음 -> 경계 볼때 한번 더 생각하기
나와 같은 경우일 경우를 빼야함
후반부에 두개가 다 있을 수도 있음... 문제를 완전 잘못 이해함. ㅜㅜ

'''
# hashmap 으로 푸는 문제

class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        idx_map = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in idx_map:
                return [idx_map[compliment], i]
            idx_map[nums[i]] = i
        return []

if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([1,3,4,2],6))