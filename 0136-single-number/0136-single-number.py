class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d1={}
        for element in nums:
            if element in d1:
                d1[element]=d1[element]+1
            else:
                d1[element]=1
        for key, value in d1.items():
            if value==1: 
                    return key

        