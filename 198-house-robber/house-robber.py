class Solution:
    def rob(self, nums: list[int]) -> int:
        dp=[-1]*len(nums)

        return self.solve(len(nums)-1,nums,dp)
    def solve(self,index,nums,dp):
        if index==0:
            return nums[0]
        if index<0:
            return 0
        if dp[index]!=-1:
            return dp[index]

        pick=nums[index]+self.solve(index-2,nums,dp)
        notpick=self.solve(index-1,nums,dp)
        dp[index]=max(pick,notpick)
        return dp[index]

