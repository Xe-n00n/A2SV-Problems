class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        smallest_idx = float('inf')
        result = []
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    if i+j <= smallest_idx:
                        smallest_idx = i+j
        
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j] and i+j == smallest_idx:
                    result.append(list1[i])

        return result