"""Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:

Players take turns placing characters into empty squares ' '.
The first player A always places 'X' characters, while the second player B always places 'O' characters.
'X' and 'O' characters are always placed into empty squares, never on filled ones.
The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".

You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first."""
class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        grid = [[' ' for _ in range(3)] for _ in range(3)]
        player = 'A'
        for i in moves:
            row,col =i
            grid[row][col] = player
            if (
                     (grid[row][0] == grid[row][1] == grid[row][2] == player) or
                     (grid[0][col] == grid[1][col] == grid[2][col] == player) or 
                     (row == col and grid[0][0] == grid[1][1] == grid[2][2] == player) or 
                     (row + col == 2 and grid[0][2] == grid[1][1] == grid[2][0] == player) 
            ):
                      return player
            if player == 'A':
                     player= 'B' 
            else:
                    player='A'
        if len(moves) == 9 :
            return "Draw" 
        else:
            return "Pending"
sl=Solution()
sl.tictactoe
