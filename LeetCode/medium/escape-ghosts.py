class Solution:
    def manhatten_distance(self, point1,point2):
        return abs(point1[0]-point2[0])+abs(point1[1]-point2[1])

    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        distance = self.manhatten_distance(target, [0,0])
        for ghost in ghosts:
            if distance >= self.manhatten_distance(ghost,target):
                return False

        return True