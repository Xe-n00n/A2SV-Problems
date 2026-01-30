class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_string = min(strs, key=len)
        min_length = len(shortest_string)
        if min_length == 0:
            return ""
        common = ''
        continue_search = True
        current = strs[0][0]
        current_length = 0
        while current_length < min_length and continue_search :
            for string in strs:
                if string[current_length] != current:
                    continue_search=False
            
            if continue_search == True:
                common += string[current_length]
            
            current_length += 1  
            if current_length < min_length:  
                current = string[current_length]

        return common




                
            
                
            
        
            

        