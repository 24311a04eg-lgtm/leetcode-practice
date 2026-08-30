class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        for val in range(0,n+1):
            if val not in nums:
                return val

        
        
        