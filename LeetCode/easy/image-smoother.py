class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        matrix = []
        for i in range(len(img)): 
            line = []
            for j in range(len(img[0])): 
                average = 0
                ops_number = 0
                for x in range(i-1,i+2): 
                    if x < 0 or x > len(img)-1:
                        continue
                    for y in range(j-1,j+2):
                        if y < 0 or y > len(img[0])-1:
                            continue
                        average += img[x][y]
                        ops_number += 1
                average = average // ops_number     
                line.append(average)
            matrix.append(line)
        return matrix
        