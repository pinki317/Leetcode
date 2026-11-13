class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        arr=sorted(nums1+nums2)
        n=len(arr)
        if n%2!=0:
            return arr[n//2]
        else:
            return (arr[n//2-1]+arr[n//2])/2
        