class Solution:
    def searchRange(self, nums, target):
        return [self.findfirst(nums,target),self.findlast(nums,target)]

    def findfirst(self,nums,target):

            n=len(nums)
            low=0
            high=n-1
            ans=-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
                    ans=mid
                    high=mid-1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return ans
    def findlast(self,nums,target):

            n=len(nums)
            low=0
            high=n-1
            ans=-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
                    ans=mid
                    low=mid+1
                elif nums[mid]>target:
                    high=mid-1
                else:
                    low=mid+1
            return ans

        
                