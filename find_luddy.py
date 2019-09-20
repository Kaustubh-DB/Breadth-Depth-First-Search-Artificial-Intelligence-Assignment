#!/usr/local/bin/python3
#
# find_luddy.py : a simple maze solver
#
# Submitted by : [Kaustubh Bhalerao, kbhaler@iu.edu]
#
# Based on skeleton code by Z. Kachwala, 2019
#

import sys
import collections


def convertTuple(tup):
    str = ''.join(tup)
    return str


# Parse the map from a given filename
def parse_map(filename):
    with open(filename, "r") as f:
        return [[char for char in line] for line in f.read().split("\n")]


# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
    return 0 <= pos[0] < n and 0 <= pos[1] < m


# Find the possible moves from position (row, col)
def moves(map, row, col):
    moves = ((row + 1, col), (row - 1, col), (row, col - 1), (row, col + 1))
    # print(moves)
    # print(map[0])

    # Return only moves that are within the board and legal (i.e. on the sidewalk ".")
    return [move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@")]


# Defines the Path of the traversal, N: If its north, S: If its South, E: If its East, W:
def find_path(row, col, or_row, or_col):
    if row == or_row - 1:
        return 'N'
    if row == or_row + 1:
        return 'S'
    if col == or_col - 1:
        return 'W'
    if col == or_col + 1:
        return 'E'


# Perform search on the map, visited array is defined to reduce the number of states to explore
def search1(IUB_map):
    # Find my start position
    you_loc = [(row_i, col_i) for col_i in range(len(IUB_map[0])) for row_i in range(len(IUB_map)) if
               IUB_map[row_i][col_i] == "#"][0]
    fringe = [(you_loc, 0, '')]
    visited_node = []
    # print(IUB_map[0])
    while fringe:
        (curr_move, curr_dist, path) = fringe.pop(0)
        # print("--------------")
        if IUB_map[curr_move[0]][curr_move[1]] == "@":
            return str(curr_dist) + '  ' + path
        # visited.append(curr_move)
        for move in moves(IUB_map, *curr_move):
            # print("This is current move", curr_move)
            # print("This is move",move)
            direction = find_path(*move, *curr_move)
            if move not in visited_node:
                # print("This is the move taken to add to fringe",move)
                visited_node.append(move)
                # print("VISITED **********",visited)
                fringe.append((move, curr_dist + 1, path + direction))
    return 'Inf'


# Returns Inf if solution is not found and is going into an infinte loop.

# Main Function
if __name__ == "__main__":
    IUB_map = parse_map(sys.argv[1])
    path = ''
    print("Shhhh... quiet while I navigate!")
    solution = search1(IUB_map)
    print("Here's the solution I found:")
    print(solution)
