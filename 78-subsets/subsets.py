class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result=[]
        temp=[]
        self.solve(0,nums,temp,result)
        return result
    
        
    def solve(self,i,nums,temp,result):
        if i>=len(nums):
            result.append(temp.copy())
            return 
        temp.append(nums[i])
        self.solve(i+1,nums,temp,result)
        temp.pop()
        self.solve(i+1,nums,temp,result)
        


         
        