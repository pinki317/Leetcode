class Solution:
    def search(self, nums: list[int], target: int) -> int:
        return self.binarysea(nums,0,len(nums)-1,target)
    def binarysea(self,nums,l,r,target):
        if l>r:
            return -1
        mid=l+(r-l)//2
        if nums[mid]==target:
            return mid
        if nums[mid]<target:
            return self.binarysea(nums,mid+1,r,target)
        return self.binarysea(nums,l,mid-1,target)
       # n=len(nums)
        #low=0
        #high=n-1
        #while low<=high:
         #   mid=(low+high)//2
          #  if nums[mid]==target:
           #     return mid
           # elif nums[mid]<target:
            #    low=mid+1
            #else:
             #   high=mid-1
      #  return -1
        