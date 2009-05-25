#!/usr/bin/env python2.6
import sys
import os
Board = [[0 for x in xrange(9)] for y in xrange(9)]

# read in file describing a board 
# file can have any number of values per line
# so long as they are not delimited by anything
def readBoardByNoDelim(filename):
    of=open(filename,"r")
    x=0
    y=0
    for line in of.readlines():
        for sq in line:
            if sq.isdigit() == False:
                sq = 0
            Board[y][x]=int(sq)
            x+=1
            if x == 9:
                x=0
                y+=1
            if y == 9:
                break
        if y == 9:
            print 'File has more values than 9x9 sudokuboard'
            break

# read in file describing a board 
# file can have any number of values per line
# so long as they are delimited by spaces
def readBoardBySpaceDelim(filename):
    of=open(filename,"r")
    x=0
    y=0
    for line in of.readlines():
        for sq in line.split():
            if sq.isdigit() == False:
                sq = 0
            Board[y][x]=int(sq)
            x+=1
            if x == 9:
                x=0
                y+=1
            if y == 9:
                break
        if y == 9:
            print 'File has more values than 9x9 sudokuboard'
            break

def readBoardByCoords(filename):
    # open the file
    of=open(filename,"r")
    numlines=int(of.readline())

    # read in the board
    x=0
    y=0
    for q in range(0,numlines-1):
        items=of.readline().split()
        Board[int(items[1])][int(items[0])]=int(items[2])
    of.close()

# Prints the space delimited sudoku board
def printBoard():
    for x in xrange(9):
        s = ''
        for y in xrange(9):
            s+=str(Board[y][x]) + ' '
        print s


def possible(y,x,value):
    if x > 8 or x < 0 or y > 8 or y < 0:
        raise Exception('index out of bounds')

    #check column 
    for i in xrange(9):
        if Board[i][x] == value:
            return False

    #check row
    for i in xrange (9):
        if Board[y][i] == value:
            return False

    #check square 3x3
    low_x=x-x%3
    low_y=y-y%3

    for i in xrange(low_x,low_x+3):
        for j in xrange(low_y,low_y+3):
            if Board[j][i] == value:
                return False

    return True

def solve():
    attempting=1 #the attempting value we checked at that spot
    x=0 #row
    y=0 #col
    possibilities=0
    while True:
        if Board[y][x] == 0:
            while(attempting <= 9):
                if possible(y,x,attempting):
                    Board[y][x] = attempting
                    possibilities += solve()
                attempting+=1

            Board[y][x]=0
            return possibilities
        elif x < 8:
            x+=1
        elif x == 8 and y < 8:
            x=0
            y+=1
        else:
            possibilities += 1
            # printBoard()
            return possibilities

def main():
    if len(sys.argv) == 3:
        if sys.argv[1] == '-c':
            readBoardByCoords(sys.argv[2])
        elif sys.argv[1] == '-s':
            readBoardBySpaceDelim(sys.argv[2])
        elif sys.argv[1] == '-n':
            readBoardByNoDelim(sys.argv[2])
        else:
            sys.exit('switch \''+ sys.argv[1] +'\' not expected') 
    else:
        print "USAGE: sudoku.py [-c] filename \n\n -c  for boards by coordinates\n -s  for boards delimited by spaces\n-n  for boards with no delimiters"
        sys.exit("missing params")
    printBoard()

    pos=solve()
    print 'pos:' + str(pos)


main()
