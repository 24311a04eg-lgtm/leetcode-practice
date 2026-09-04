class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        n=len(nums)
        for val in nums:
            if val not in freq:
                freq[val]=1
            else:
                freq[val]+=1
        for val, count in freq.items():
            if count > n // 2:
               return val
        
        



        