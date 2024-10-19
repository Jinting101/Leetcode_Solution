# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        # matrix = [[-1] * n for _ in range(m)]
        # flag = 'r'
        # row, col = 0, 0

        # while head:
        #     matrix[row][col] = head.val

        #     # Determine the next direction
        #     if flag == 'r' and (col + 1 >= n or matrix[row][col + 1] != -1):
        #         flag = 'd'
        #     elif flag == 'd' and (row + 1 >= m or matrix[row + 1][col] != -1):
        #         flag = 'l'
        #     elif flag == 'l' and (col - 1 < 0 or matrix[row][col - 1] != -1):
        #         flag = 'u'
        #     elif flag == 'u' and (row - 1 < 0 or matrix[row - 1][col] != -1):
        #         flag = 'r'

        #     # Move based on the current direction
        #     if flag == 'r':
        #         col += 1
        #     elif flag == 'd':
        #         row += 1
        #     elif flag == 'l':
        #         col -= 1
        #     elif flag == 'u':
        #         row -= 1

        #     # If the next position is already filled, break
        #     if row >= m or col >= n or row < 0 or col < 0 or matrix[row][col] != -1:
        #         break

        #     head = head.next

        # return matrix

        # Initialize matrix with -1
        matrix = [[-1] * n for _ in range(m)]

        # Initialize direction flags
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        dir_index = 0
        
        # Initialize current position
        row, col = 0, 0
        
        while head:
            # Fill current cell with value from linked list
            matrix[row][col] = head.val
            
            # Determine next direction
            next_row, next_col = row + directions[dir_index][0], col + directions[dir_index][1]
            
            # Check if next position is valid
            if (0 <= next_row < m and 0 <= next_col < n and 
                matrix[next_row][next_col] == -1):
                row, col = next_row, next_col
            else:
                # Change direction
                dir_index = (dir_index + 1) % 4
                row, col = row + directions[dir_index][0], col + directions[dir_index][1]
            
            # Move to next node in linked list
            head = head.next
        
        return matrix

# Initialize an empty matrix of size m x n with all values set to -1.
# Set the initial direction to right (r).
# Start from the top-left corner of the matrix (position [0, 0]).

# For each node in the linked list:
# Place its value in the current matrix cell.
# Depending on the current direction (r, d, l, or u), attempt to move to the next cell.
# If moving in the current direction leads outside the matrix or to an already filled cell, change the direction (from right to down, from down to left, etc.).

# Continue until all nodes are processed or the matrix is completely filled.
# If there are leftover matrix cells and no more list nodes, leave them as -1.