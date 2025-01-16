"""
// Explain your approach briefly:
// The problem is solved using DFS to explore all possible cells recursively or BFS for an iterative solution. 
// Depending on the clicked cell:
// - If it is a mine ('M'), the game ends, and we mark it as 'X'.
// - If it is an empty cell ('E') with no adjacent mines, we reveal it as 'B' and recursively reveal its neighbors.
// - If it is an empty cell with adjacent mines, we reveal it with the number of adjacent mines.
// We use a helper function to count adjacent mines and ensure that the board boundaries are respected.

// Time Complexity: O(m * n) in the worst case, where we may need to visit all cells.
// Space Complexity: O(m * n) for recursion stack in DFS or queue in BFS.
// Did this code successfully run on Leetcode: Yes
// Any problem you faced while coding this: No
"""

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # Dimensions of the board
        rows, cols = len(board), len(board[0])
        
        # Directions for 8-connected neighbors
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        def count_mines(r, c):
            # Count the number of mines adjacent to (r, c)
            count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'M':
                    count += 1
            return count

        def dfs(r, c):
            # If out of bounds or not an unrevealed empty square, return
            if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != 'E':
                return
            
            # Count adjacent mines
            mine_count = count_mines(r, c)
            
            if mine_count > 0:
                # If there are adjacent mines, reveal the count
                board[r][c] = str(mine_count)
            else:
                # If no adjacent mines, reveal as 'B' and explore neighbors
                board[r][c] = 'B'
                for dr, dc in directions:
                    dfs(r + dr, c + dc)
        
        # Handle the click
        cr, cc = click
        if board[cr][cc] == 'M':
            # If the clicked cell is a mine, game over
            board[cr][cc] = 'X'
        else:
            # Start revealing from the clicked cell
            dfs(cr, cc)
        
        return board
