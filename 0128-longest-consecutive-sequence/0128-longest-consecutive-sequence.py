class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        count=1
        max_count=1
        if n==0:
            return 0
        for i in range(n-1):
            if nums[i+1] == nums[i]:
                pass
            elif nums[i+1] == nums[i] + 1:
                count+=1
            else:
                max_count=max(max_count,count)
                count=1
        return max(max_count,count)           






        
        