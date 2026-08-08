class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[]
        seen=set(nums)
        for val in range(1,n+1):
            if val not in seen:
                result.append(val)
        return result


        