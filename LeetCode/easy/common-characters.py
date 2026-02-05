from collections import Counter


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        chars_map1 = Counter(words[0])
        for word in words:
            chars_map2 = Counter(word)
            for c in list(chars_map1.keys()):
                if c in chars_map2:
                    chars_map1[c]=min(chars_map1[c],chars_map2[c])
                else:
                    del chars_map1[c]

        result = []
        for c in chars_map1.keys():
            result.extend(c * chars_map1[c])

        return result

        
        