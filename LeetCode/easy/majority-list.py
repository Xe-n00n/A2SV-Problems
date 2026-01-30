class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements_dict={}
        for num in nums:
            if num in elements_dict:
                elements_dict[num]+=1
            else:
                elements_dict[num]=1
                
        sorting=sorted(elements_dict.items(),key=lambda item: item[1])
        print(sorting)
        return sorting[-1][0]