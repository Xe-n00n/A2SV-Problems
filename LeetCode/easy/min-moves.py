class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats = sorted(seats)
        students = sorted(students)
        total_moves = [abs(student - seat) for student, seat in zip(students,seats)]
        return sum(total_moves)