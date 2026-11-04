class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        low=max(nums)
        high=sum(nums)
        ans=high
        while low<=high:
            mid=(low+high)//2
            if self.cansplit(nums,k,mid):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
    def cansplit(self,nums,k,maxsum):
        count=1
        currsum=0
        for num in nums:
            if currsum+num<=maxsum:
                currsum+=num
            else:
                count+=1
                currsum=num
        return count<=k