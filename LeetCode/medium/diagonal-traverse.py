class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result = []
        m = len(mat)
        n = len(mat[0])
        for index in range(m+n-1):            
            if index%2 == 0:
                start = max(0,index - n+1)
                end = min(index, m-1)
                for i in range(end,start-1,-1):
                    result.append(mat[i][index-i])
            
            else:
                start = max(0,index - n+1)
                end = min(index, m-1)
                for i in range(start,end+1):
                    result.append(mat[i][index-i])

        return result