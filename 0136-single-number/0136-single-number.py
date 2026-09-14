class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n=len(nums)
        freq={}
        for val in nums:
            if val in freq:
                freq[val]+=1
            else:
                freq[val]=1
        for val in nums:
            if freq[val]==1:
                return val


        