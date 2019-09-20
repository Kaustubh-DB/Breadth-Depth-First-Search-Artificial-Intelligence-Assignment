# a0 

Part 1: Finding Your Way

Python program for Finding Your Way from a given location to the final location.
This program demonstrates search algorithm named Breadth First Search. It basically finds for best possible shortest path for a given set of input map. The set of components for the program are: 1] The map given in a ‘.Txt’ File. 2] Certain blocked positions are marked by ‘&’. 3] The starting position marked by #. 4] A end position or the target position marked by @.
Solution of Finding Your Way problem we check the possible valid paths that is, all the (‘.‘) positions, in the same row and in the same column, starting with the ‘#’, and moving onto the next valid adjacent nodes, considering & as a block-way and thereby restricting its path. 
State of states will be all the possible moves from # point to @. Initial state will be the starting location of traversal(#). Successor function Succ:S will be all the valid positions(“.”) in the same row and column for that particular state.  

Observations and Experiment,
At the first point, Initial node is inserted into the fringe, and then popped out(Queue approach) and its valid successor is being appended to the fringe. And this task is being carried out until we reach our goal state. At Initial stage, main difficulty that I found going through this code was it was going in infinite loop as it was searching for all possible moves, and also considered the recurring moves. Hence, to reduce the number of states I used visited_node list, thereby adding visited states into fringe. Also to get all the possible directions(N,S,W,E), I passed *move(present) and *curr_move(successor) to see the comparison between row or column values, for instance if curr_move’s row valueis 1 less than move’s value then it is travelling North so used literal ‘N’ and thereby appended it in the fringe along with the cost of moving to its successor node that is 1. This loop was carried until we reached our goal state thereby increasing its distance by one while moving to its successor and adding path of its traversal. Also if solution is not found, and is going into infinite loop then it will return Inf. 



Part 2: Hide and Seek

Python program for arranging K friends, such that no two friends can see one another.
This program demonstrates search algorithm named Depth First Search. The set of components for the program are: 1] The map given in a ‘.Txt’ File. 2] Certain blocked positions that are marked by ‘&’.
Solution of arranging is that we iterate from left to right and top to bottom over the map to get the first empty position. So now is the time where we can place the 1st Friend at that point. The Initial State will be defined by placing the first friend and moving this state to the fringe. Successor function Succ:S will be all the valid position that the second friend could be placed with a condition that it can’t be placed in the same row, column respective to the friend. New Friend can only be placed after the block between the same row and column. Check if new friend is visible on the east, west, south and north from this side walk, if the friend is not visible in the same path, then place that friend on the board and push it on the fringe. Check this loop till all the friends are placed and no more fringe items are left. That will be our goal state.


Observation and Experiment,
At the initial stage, I was stuck with a problem of exploring all the possible states including the one that is visited recursively for the same row and column, I thereby reduced the number of states to explore by adding traversed states list in the fringe. I made a try to use recursive method in a way to avoid using fringe but was not able to do so. Hence maximizing the time complexity of the code. The code can be made more optimizable by breaking the loop for traversal if we are not able to find the friend’s placement in the same row or column after the first iteration and was not able to achieve that goal. I will in fact try to learn more about recursive functionality and avoiding unnecessary loop traversals in the coming weeks and try to implement it in the next assignment making the code optimum as possible. 
