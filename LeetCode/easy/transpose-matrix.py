class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose=[]
        for j in range(len(matrix[0])):
            line = []
            for i in range(len(matrix)):
                line.append(matrix[i][j])
            transpose.append(line)

        return transpose

        