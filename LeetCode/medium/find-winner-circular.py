class Solution:
    def next_out(self,n,i,k):
        return (i+k-1)%n
        
    def findTheWinner(self, n: int, k: int) -> int:
        current_position = 0
        next_out = -1
        participants = list(range(1,n+1))
        participants_length = n

        while participants_length > 1:
            next_out = self.next_out(participants_length,current_position,k)
            participants.pop(next_out)
            current_position = next_out
            participants_length -= 1
        

        return participants.pop()