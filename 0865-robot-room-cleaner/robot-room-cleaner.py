# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        #up, right, down, left
        directions = [(-1,0), (0,1), (1,0),(0,-1)]
        visit = set()
        
        
        def move_back():
            #^ > V
            #^ < V
            #  
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def backtrack(row, col, direction):
            #mark current position as visited
            visit.add((row,col))
            robot.clean() #clean current cell

            for i in range(4):
                #direction=0(up)|1(right) and so on
                new_direction = (direction+i)%4

                new_row = row + directions[new_direction][0]
                new_col = col + directions[new_direction][1]

                #we will visit the new position
                if (new_row, new_col) not in visit and robot.move():
                    #recursively explore new position
                    backtrack(new_row, new_col, new_direction)
                    #move back after exploration
                    move_back()
                
                robot.turnRight()
    
        backtrack(0,0,0)