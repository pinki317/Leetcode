class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n=len(nums)
        k=k%n
        def reverse(low,high):
            while low< high:
                nums[low],nums[high]=nums[high],nums[low]
                low+=1
                high-=1
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)
        
        