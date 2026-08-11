class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        n=len(nums)
        for val in nums:
            ans.append(val)
        for val in nums:
            ans.append(val)
        return ans
        