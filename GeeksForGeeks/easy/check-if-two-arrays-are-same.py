class Solution:
    def checkEqual(self, a, b) -> bool:
        if sorted(a)==sorted(b): 
            return True
        else:
            return False