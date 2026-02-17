class Solution:
    def explore_level(self,matrix,top, bottom,left,right):
        result = []
        for i in range(left,right+1):
            result.append(matrix[top][i])
        for j in range(top+1,bottom+1):
            result.append(matrix[j][right])
        if top < bottom:
            for k in range(right-1,left-1,-1):
                result.append(matrix[bottom][k])
        if left < right:
            for s in range(bottom-1,top,-1):
                result.append(matrix[s][left])
        return result


    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        top,left,bottom,right = 0,0,len(matrix)-1,len(matrix[0])-1
        while top <= bottom and left <= right: 
            exploration = self.explore_level(matrix,top,bottom,left,right) 
            result.extend(exploration)
            top += 1
            left += 1
            right -= 1
            bottom -= 1
            
        return result

            