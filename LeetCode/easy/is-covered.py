class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        verified_condition=True
        num=left
        while num <right+1 and verified_condition:
            for range_value in ranges:
                if num>=range_value[0] and num<=range_value[1]:
                    verified_condition=True
                    break
                else:
                    verified_condition=False
            num+=1
            
        return verified_condition
        