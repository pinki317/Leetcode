class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        rows=len(matrix)
        cols=len(matrix[0])
        heights=[0]*cols
        maxarea=0
        for i in range(0,rows):
            for j in range(0,cols):
                if matrix[i][j]=='1':
                    heights[j]+=1
                else:
                    heights[j]=0
                
            maxarea=max(maxarea,self.largestArea(heights))
        return maxarea
    def largestArea(self,heights):
        n=len(heights)
        st=[]
        maxarea=0
        for i in range(n+1):
            h=0 if i==n else heights[i]
            while st and h<heights[st[-1]]:
                height=heights[st.pop()]
                w=i if not st else i-st[-1]-1
                area=height*w
                maxarea=max(maxarea,area)
            st.append(i)
        return maxarea
        