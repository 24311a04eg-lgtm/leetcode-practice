class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        self.st=[]
        n=len(num)
        for i in range(0,n):
            while(self.st and k>0 and self.st[-1] > num[i]):
                self.st.pop()
                k=k-1
            self.st.append(num[i])
        while(k>0):
            self.st.pop()
            k=k-1
        
        ans = "".join(self.st)

        ans = ans.lstrip('0')

    
        if ans == "":
            return "0"

        return ans


        