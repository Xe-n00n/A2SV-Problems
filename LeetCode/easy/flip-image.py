class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        matrix = []
        for i in range(len(image)):
            line = []
            for j in range(len(image[0])-1,-1,-1):
                line.append(1 ^ image[i][j])
            matrix.append(line)
        return matrix
