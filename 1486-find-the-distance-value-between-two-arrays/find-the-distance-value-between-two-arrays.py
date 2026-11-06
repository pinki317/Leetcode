class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        count=0
        for num in arr1:
            left=0
            right=len(arr2)-1
            valid=True
            while left<=right:
                mid=(left+right)//2
                if abs(num-arr2[mid])<=d:
                    valid=False
                    break
                elif arr2[mid] <num:
                    left=mid+1
                else:
                    right=mid-1
            if valid:
                count+=1
        return count

