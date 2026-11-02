class Solution:
    def minDays(self, bloom: list[int], m: int, k: int) -> int:
        n=len(bloom)
        if m*k>n:
            return -1
        low=min(bloom)
        high=max(bloom)
        ans=-1
        while low<=high:
            mid=(low+high)//2
            if self.canmake(bloom,m,k,mid):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
    def canmake(self,bloom,m,k,day):
        count=0
        boq=0
        for flowers in bloom:
            if flowers<=day:
                count+=1
                if count==k:
                    boq+=1
                    count=0
            else:
                count=0
        return boq>=m        