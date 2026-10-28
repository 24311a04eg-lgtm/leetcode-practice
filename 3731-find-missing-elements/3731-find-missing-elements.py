class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        arr=[]
        maxi=nums[0]
        mini=nums[0]
        n=len(nums)
        for i in range(n):
            maxi=max(maxi,nums[i])
            mini=min(mini,nums[i])
        for val in range(mini,maxi+1):
            if val not in nums:
                arr.append(val)
        return arr

        