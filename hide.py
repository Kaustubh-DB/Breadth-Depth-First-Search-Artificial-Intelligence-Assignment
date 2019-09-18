#!/usr/local/bin/python3
#
# hide.py : a simple friend-hider
#
# Submitted by : [Kaustubh Bhalerao, kbhaler@iu.edu]
#
# Based on skeleton code by D. Crandall and Z. Kachwala, 2019
#
# The problem to be solved is this:
# Given a campus map, find a placement of F friends so that no two can find one another.
#

import sys

# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().split("\n")]

# Count total # of friends on board

# Return a string with the board rendered in a human-friendly format
def printable_board(board):
    return "\n".join([ "".join(row) for row in board])

# Add a friend to the board at the given position, and return a new board (doesn't change original)
def add_friend(board, row, col):
    return board[0:row] + [board[row][0:col] + ['F',] + board[row][col+1:]] + board[row+1:]

#Check the position of
def checkposition_up(board, r, c):

    for row_board in range(r,-1,-1):
        if(board[row_board][c]== '&'):
            return True
        if(board[row_board][c] == 'F'):
            return False
    return True

def checkposition_down(board, r, c):
    for row_board in range(r,len(board)):
        if(board[row_board][c]== '&'):
            return True
        if(board[row_board][c] == 'F'):
            return False
    return True

def checkposition_left(board, r, c):

    for col_board in range(c,-1,-1):
        if(board[r][col_board]== '&'):
            return True
        if(board[r][col_board] == 'F'):
            return False
    return True

def checkposition_right(board, r, c):
    #5th row and 4th column

    for col_board in range(c,len(board[0])):
        if(board[r][col_board]== '&'):
            return True
        if(board[r][col_board] == 'F'):
            return False
    return True

# Get list of successors of given board state
def successors(board):
    #visited=[]
   # friends_number = count_friends(board)
    arr = []
    for r in range(0, len(board)):
        for c in range(0, len(board[0])):
            if board[r][c] == '.':
               if checkposition_up(board,r,c):
                   if checkposition_down(board,r,c):
                       if checkposition_left(board,r,c):
                           if checkposition_right(board,r,c):
                                    arr.append(add_friend(board,r,c))

    return arr
    #return [add_friend(board, r, c) for r in range(0, len(board)) for c in range(0,len(board[0])) if board[r][c] == '.']

# check if board is a goal state
def is_goal(board):
    return count_friends(board) == K

def count_friends(board):

    count =0
    #print("The Sum is:",sum([row.count('F') for row in board]))
    return sum([row.count('F') for row in board])
# Solve n-rooks!


def solve(initial_board):
    visited =[]
    fringe = [initial_board]
    while len(fringe) > 0:
        for s in successors(fringe.pop()):
            if s not in visited:
                if is_goal(s):
                    return(s)
                fringe.append(s)
                visited.append(s)
    return False

# Main Function
if __name__ == "__main__":
    IUB_map=parse_map(sys.argv[1])
    # This is K, the number of friends
    K = int(sys.argv[2])
    print ("Starting from initial board:\n" + printable_board(IUB_map) + "\n\nLooking for solution...\n")
    solution = solve(IUB_map)
    print ("Here's what we found:")
    print (printable_board(solution) if solution else "None")
