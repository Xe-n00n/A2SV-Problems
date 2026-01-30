
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # structure: playerNumber: [wins, losts]
        dictionary={} 
        wins_only=[]
        one_lost=[]
        for match in matches:
            if match[0] in dictionary.keys():
                dictionary[match[0]][0]+=1
            else: 
                dictionary[match[0]]=[1,0]
            
            if match[1] in dictionary.keys():
                dictionary[match[1]][1]+=1

            else:
                dictionary[match[1]]=[0,1]

        for element in dictionary.keys():
            if dictionary[element][1] == 0:
                wins_only.append(element)
            
            if dictionary[element][1] == 1:
                one_lost.append(element)
        
        return [sorted(wins_only),sorted(one_lost)]