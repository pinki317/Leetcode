class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m=len(nums1)
        n=len(nums2)
        total=m+n
        i,j,prev,curr=0,0,0,0
        for _ in range(total//2+1):
            prev=curr
            if i<m and j<n:
                if nums1[i]<=nums2[j]:
                    curr=nums1[i]
                    i+=1
                else:
                    curr=nums2[j]
                    j+=1
            elif i<m:
                curr=nums1[i]
                i+=1
            else:
                curr=nums2[j]
                j+=1
        if total%2==1:
            return curr
        return (prev+curr)/2.0