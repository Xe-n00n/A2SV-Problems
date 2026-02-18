class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for j in range(len(matrix)):
            for i in range(j,len(matrix)):
                matrix[j][i], matrix[i][j]=matrix[i][j], matrix[j][i] 

        
        for j in range(len(matrix)):
            for i in range(len(matrix)//2):
                matrix[j][i], matrix[j][len(matrix)-i-1] = matrix[j][len(matrix)-i-1],matrix[j][i]