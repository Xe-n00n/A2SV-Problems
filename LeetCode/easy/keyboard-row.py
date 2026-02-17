class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set('qwertyuiop')
        row2 = set('asdfghjkl')
        row3 = set('zxcvbnm')
        result = []

        for word in words:
            w = word.lower()

            if w[0] in row1:
                for char in w:
                    if char not in row1:
                        break
                else:
                    result.append(word)

            elif w[0] in row2:
                for char in w:
                    if char not in row2:
                        break
                else:
                    result.append(word)

            elif w[0] in row3:
                for char in w:
                    if char not in row3:
                        break
                else:
                    result.append(word)

        return result
