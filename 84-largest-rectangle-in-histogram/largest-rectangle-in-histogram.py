class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n=len(heights)
        st=[]
        maxarea=0
        for i in range(n+1):
            h=0 if i==n else heights[i]
            while st and h <heights[st[-1]]:
                height=heights[st.pop()]
                width=i if not st else i-st[-1]-1
                area=width*height
                maxarea=max(maxarea,area)
            st.append(i)
        return maxarea