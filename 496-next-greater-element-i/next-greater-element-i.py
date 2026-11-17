class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:

        ans=[]
        for i in range(len(nums1)):
            next=-1
            for j in range(len(nums2)):
                if nums2[j]==nums1[i]:
                    for k in range(j+1,len(nums2)):
                        if nums2[k]>nums1[i]:
                            next=nums2[k]
                            break
                    break
            ans.append(next)
        return ans
            
        