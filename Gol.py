import sys
import copy
from time import sleep
import os

def printBoard(board, gen):
    print "Gen {}".format(gen)
    print " ",
    for col in range(1, size-1):
        print (col % 10),
    print
    for row in range(1, size-1):
        print (row % 10), 
        for col in range(1, size-1):
            print board[row][col],
        print

def computeNextGen(board):
    newboard = copy.deepcopy(board)
    for row in range(1, size-1):
        for col in range(1, size-1):
            neighbours = countNeighbours(board, row, col)
            # if the cell in question was alive to begin with
            if (board[row][col] == "*"):
                # and has either less than 2 or more than 3 neighbours
                if (neighbours < 2 or neighbours > 3):
                    # then it becomes dead
                    newboard[row][col] = " "
            else:
                # if the cell was dead to begin with, and has 3
                # neighbours
                if (neighbours == 3):
                    # then it becomes alive
                    newboard[row][col] = "*"
    return newboard

def countNeighbours(board, row, col):
    neighbours = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (not (i == 0 and j == 0)):
                if (board[row+i][col+j] == "*"):
                    neighbours += 1
    return neighbours



board = []

for line in sys.stdin:
    size = len(line) - 1
    board.append([])
    for i in range(size):
        board[len(board) - 1].append(line[i])

os.system("clear")
printBoard(board, 0)
for gen in range(10):
    sleep(0.5)
    os.system("clear")
    board = computeNextGen(board)
    printBoard(board, gen)








