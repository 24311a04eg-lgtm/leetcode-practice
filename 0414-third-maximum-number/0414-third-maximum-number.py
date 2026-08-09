class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        count=0
        n=len(nums)
        for i in range(n-1,-1,-1):
            if i == len(nums) - 1 or nums[i] != nums[i + 1]:
                count+=1
            if count == 3:
                return nums[i]

        return nums[-1]

        