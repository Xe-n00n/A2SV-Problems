class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_codes=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result = set()
        for word in words:
            translation = ''
            for c in word:
                position = ord(c.lower()) - 97
                translation += morse_codes[position]
            
            result.add(translation)
        
        return len(result)