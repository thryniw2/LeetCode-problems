# Problem 2022-05-11
# https://leetcode.com/problems/count-sorted-vowel-strings/
# Language: Python3


class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        ends = [1,1,1,1,1]
        for i in range(1,n):
            for s in range(len(ends)-1,-1,-1):
                ends[s] += sum(ends[0:s])
                
        perm = sum(ends)
            
        return perm
