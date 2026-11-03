
class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        position.sort()
        n=len(position)
        ans = 0
        low = 1
        high = position[n-1] - position[0]
        while (low<=high):
            mid=(low+high)//2
            if self.canplace(position,m,mid):
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans
    def canplace(self,position,m,gap):
        count=1
        last=position[0]
        for i in range(1,len(position)):
            if position[i]-last>=gap:
                count+=1
                last=position[i]
            if count>=m:
                return True
        return False


        