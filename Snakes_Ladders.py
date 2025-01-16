# Explain your approach in brief:
# This problem can be solved using Breadth-First Search (BFS), as it involves finding the shortest path.
# The board is treated as a graph where each square is a node, and edges exist between a square and its next 6 reachable squares.
# BFS ensures we explore all possibilities level by level to find the minimum number of moves required to reach the last square.

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # Get board size
        n = len(board)
        
        # Function to convert square number to (row, col)
        def get_coordinates(square: int) -> (int, int):
            quot, rem = divmod(square - 1, n)
            row = n - 1 - quot  # Rows are numbered from the bottom
            col = rem if row % 2 != n % 2 else n - 1 - rem  # Handle alternating directions
            return row, col

        # BFS initialization
        queue = deque([(1, 0)])  # (current square, moves)
        visited = set()  # To avoid revisiting squares
        visited.add(1)
        
        while queue:
            curr, moves = queue.popleft()
            
            # If we reach the last square, return the number of moves
            if curr == n * n:
                return moves
            
            # Explore the next 6 squares
            for next_square in range(curr + 1, min(curr + 6, n * n) + 1):
                row, col = get_coordinates(next_square)
                
                # If the board has a snake or ladder, move to its destination
                final_square = board[row][col] if board[row][col] != -1 else next_square
                
                if final_square not in visited:
                    visited.add(final_square)
                    queue.append((final_square, moves + 1))
        
        # If we exhaust the queue without reaching the last square, return -1
        return -1

# Time Complexity: O(n^2) - Each square is visited at most once, and there are n^2 squares.
# Space Complexity: O(n^2) - For the visited set and BFS queue.
# Did this code successfully run on Leetcode: Yes
# Any problem you faced while coding this: Understanding the Boustrophedon pattern for indexing.
