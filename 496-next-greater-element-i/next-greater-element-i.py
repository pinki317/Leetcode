class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:

        stack=[]
        m={}
        for i in range(len(nums2)-1,-1,-1):
            while stack and stack[-1]<=nums2[i]:
                stack.pop()
            if stack:
                m[nums2[i]]=stack[-1]
            else:
                m[nums2[i]]=-1

            stack.append(nums2[i])
        ans=[]
        for num in nums1:
            ans.append(m[num])
        return ans

            
        