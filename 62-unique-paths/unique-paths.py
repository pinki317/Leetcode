class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0 for _ in range(n)] for _ in range(m)]

        return self.countpaths(m-1,n-1,dp)
    def countpaths(self,row,col,dp):
        if row==0 and col==0:
            return 1
        if row < 0 or col < 0:
            return 0
        if dp[row][col]!=0:
            return dp[row][col]

        dp[row][col]= self.countpaths(row-1,col,dp)+self.countpaths(row,col-1,dp)
        return dp[row][col]
