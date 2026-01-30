# not my solution, taken from: https://www.geeksforgeeks.org/check-if-an-array-is-subset-of-another-array-set-1/
# couldn't solve it on my own
from collections import defaultdict


class Solution:
    def isSubset(self, a, b):
        dic1 = defaultdict(lambda: 0)
        for i in a:
            dic1[i] += 1

        #iterating over b and checking if the frequency of each element in b is greater than 0 in dic1.
        for i in b:
            if dic1[i] > 0:
                dic1[i] -= 1
            else:
                return False

        return True