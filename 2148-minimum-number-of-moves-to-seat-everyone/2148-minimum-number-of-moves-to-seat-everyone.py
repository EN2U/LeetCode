class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        total_moves = 0

        seats.sort()
        students.sort()

        for i in range(len(seats)):
            total_moves += abs(seats[i] - students[i])

        return total_moves
