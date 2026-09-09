class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        count=1
        max_count=1
        if n==0:
            return 0
        for i in range(n-1):
            if nums[i]==nums[i+1]:
                pass
            elif nums[i+1]==nums[i] + 1:
                count+=1
                max_count=max(count,max_count)
            else:
                count=1
        return max_count
        