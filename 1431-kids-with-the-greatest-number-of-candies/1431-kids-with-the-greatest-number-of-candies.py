class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n=len(candies)
        max_candi=max(candies)
        for i in range(n):
            candies[i]=candies[i]+ extraCandies
            if candies[i]>=max_candi:
                candies[i]=True
            else:
                candies[i]=False
        return candies





        

        