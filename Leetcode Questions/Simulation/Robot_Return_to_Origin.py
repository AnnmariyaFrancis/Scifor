"""There is a robot starting at the position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

You are given a string moves that represents the move sequence of the robot where moves[i] represents its ith move. Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).

Return true if the robot returns to the origin after it finishes all of its moves, or false otherwise."""
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        sum=0
        list1=[]
        for i in moves:
               if i=="U":
                    list1.append(U)
               if i=="D":
                     list1.append(-U)
               if i=="L":
                     list1.append(L)
               if i=="R":
                     list1.append(-L)
        for i in list1:
              sum=sum+i
        if sum==0:
              return True
        else:
              return False
