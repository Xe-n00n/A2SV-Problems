class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        num_index = []
        result = [0] * len(nums)

        for i in range(len(nums)):
            num_index.append((nums[i], i))

        num_index.sort()

        prev_value = None
        count_smaller = 0

        for i in range(len(num_index)):
            value, original_index = num_index[i]

            if value != prev_value:
                count_smaller = i  
                prev_value = value

            result[original_index] = count_smaller

        return result
