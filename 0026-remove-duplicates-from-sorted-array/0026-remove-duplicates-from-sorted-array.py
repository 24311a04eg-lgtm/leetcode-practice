class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums2=[]
        for val in nums:
            if val not in nums2:
                nums2.append(val)
        for i in range(len(nums2)):
            nums[i] = nums2[i]
        return len(nums2)        
        

        
        