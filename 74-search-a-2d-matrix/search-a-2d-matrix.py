class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        top=0
        bottom=m-1
        row=-1
        while top<=bottom:
            mid=(top+bottom)//2
            if matrix[mid][0]<=target <=matrix[mid][n-1]:
                row=mid
                break
            elif target < matrix[mid][0]:
                bottom=mid-1
            else:
                top=mid+1
        if row== -1:
            return False
        left=0
        right=n-1
        while left<=right:
            mid=(left+right)//2
            if matrix[row][mid]==target:
                return True
            elif matrix[row][mid]<target:
                left=mid+1
            else:
                right=mid-1
        return False
            
