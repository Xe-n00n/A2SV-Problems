class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sorted_nums=sorted(nums)
        index=0
        for i in range(len(sorted_nums)):
            if i==sorted_nums[i]:
                continue
            else:
                return i
        
        return i+1
            


        