class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return 0 
        boomerangs = 0
        for i in range(len(points)):
            distances ={}
            for j in range(len(points)):
                distance =  (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2
                if distance in distances.keys():
                    distances[distance] += 1
                else:
                    distances[distance] = 1
            
            for distance in distances.keys():
                boomerangs += distances[distance]*(distances[distance]-1)

        return boomerangs
          