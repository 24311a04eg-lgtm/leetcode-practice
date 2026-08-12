class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even=[]
        odd=[]
        for val in nums:
            if val%2==0:
                even.append(val)
            else:
                odd.append(val)
        return even+odd




        