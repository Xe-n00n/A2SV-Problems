class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        sorted_nums=sorted(nums)
        previous_num=None
        result=[]
        for num in sorted_nums:
            if num == previous_num :
                result.append(num)
            previous_num=num

        return result


        