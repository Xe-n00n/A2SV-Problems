class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True        
        
        difference=0
        swappables=[]
        for c1,c2 in zip(s1,s2):
            if c1!=c2:
                difference+=1 
                swappables.append((c1,c2)) 

        
        if difference==2 and swappables[0]==swappables[1][::-1]: 
            return True
        else:
            return False
