class Solution:
    def isPalindrome(self, x: int) -> bool:

        nums = list(str(x))
        if nums[::-1]==nums:
           
            return True
        else:
            return False