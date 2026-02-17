class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        score = 0
        for i in range(len(nums)):
                nums[i] = sorted(nums[i])
        for j in range(len(nums[0])):
            maximum = 0
            for i in range(len(nums)):
                if nums[i][j]> maximum :
                    maximum = nums[i][j]
            score += maximum
        return score
