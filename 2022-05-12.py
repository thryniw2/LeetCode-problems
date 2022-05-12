# Problem 2022-05-12
# https://leetcode.com/problems/permutations-ii/
# Language: Python3

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.perms = []
        self.result = []
        self.permuteHelper([], nums)
        
        return self.result
        
    def permuteHelper(self, perm, nums):
        if nums == []:
            check = self.checksum(perm)
            if check in self.perms:
                return
                
            self.perms.append(check)
            self.result.append(perm)
            return
        
        for i in range(len(nums)):
            cur_perm = perm + [nums[i]]
            cur_nums = nums[:i] + nums[i+1:]
            self.permuteHelper(cur_perm, cur_nums)
        return
    
    def checksum(self, perm):
        total = 0
        for i in range(len(perm)):
            total += (perm[i]+10)*(21**i)
        
        return total
