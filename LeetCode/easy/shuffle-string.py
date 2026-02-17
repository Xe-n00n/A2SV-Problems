class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        string = [''] * len(indices)
        for i in range(len(indices)):
            string[indices[i]] = s[i]
        return "".join(string)