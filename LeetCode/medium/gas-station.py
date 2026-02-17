class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        -2 -2 -2  3  3 

        -2 3 -2 3 -2

        -2 3 -2 7 -2 -2 3 -2 3 -2

        -1 -1  1

        1 -3 1 -2 3
        """

        if sum(gas) - sum(cost) < 0:
            return -1

        consumption = [x-y for x,y in zip(gas,cost)]
        i = 0
        while i < len(gas):
            if consumption[i] >= 0 :
                # candidate found
                tank = consumption[i]
                for j in range(i+1, len(consumption)):
                    tank += consumption [j]
                    if tank < 0 :
                        i = j+1 
                        break

                if tank < 0 : 
                    continue
                for k in range(i):
                    tank += consumption[k]
                    if tank < 0:
                        i = j + 1
                        break

                if tank >= 0:
                    return i
            i += 1

        return -1
