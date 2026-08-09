class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        freq={}
        for val in nums1:
            if val not in freq:
                freq[val]=1
            else:
                freq[val]+=1
        for val in nums2:
            if val not in freq:
                pass
            elif freq[val]>0:
                result.append(val)
                freq[val]-=1
        return result






        

        