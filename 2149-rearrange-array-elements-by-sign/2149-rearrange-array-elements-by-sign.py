class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        for val in nums:
            if val>0:
                pos.append(val)
            else:
                neg.append(val)
        ans=[]
        for i in range(len(pos)):
            ans.append(pos[i])
            ans.append(neg[i])

        return ans



        