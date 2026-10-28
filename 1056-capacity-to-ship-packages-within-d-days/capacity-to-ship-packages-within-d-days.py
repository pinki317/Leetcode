        
class Solution:
    def shipWithinDays(self, weight: list[int], days: int) -> int:
        low=max(weight)
        high=sum(weight)
        ans=high
        while low<= high:
            mid=(low+high)//2
            if self.canship(weight,days,mid):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
    def canship(self,weight,days ,cap):
        d=1
        sum=0
        for w in weight:
            if sum+w>cap:
                d+=1
                sum=w

            else:
                sum+=w
        return d<=days
        