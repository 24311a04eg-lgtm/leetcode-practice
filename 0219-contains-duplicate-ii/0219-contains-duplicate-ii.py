class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        freq={}
        for i in range(n):
            if nums[i] in freq:
                if i-freq[nums[i]] <=k:
                    return True
            freq[nums[i]]=i
        return False
        
        