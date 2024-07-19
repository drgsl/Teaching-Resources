# N-Queens with Blocked Squares Python Solution using Forward Checking

This repository contains a Python solution for the N-Queens problem with blocked squares, implemented using forward checking. The N-Queens problem is a classic problem in computer science, which involves placing N chess queens on an N x N chessboard, so that no two queens threaten each other. This problem becomes more challenging when there are blocked squares on the board that cannot be used.

## Overview
### Board/Matrix Functions
- `printMatrix(matrix)`: prints the input matrix in a readable way
- `generateMatrix(w, h)`: generates a matrix of width w and height h
- `generateChessBoard(size)`: generates a chessboard of size x size by calling generateMatrix with size as both the width and height

### Square Writing
- `block(board, idx, jdx)`: blocks the square at the given row and column indices on the input chessboard
- `isBlocked(board, idx, jdx)`: returns true if the square at the given row and column indices on the input chessboard is blocked
- `queen(board, idx, jdx)`: places a queen on the square at the given row and column indices on the input chessboard
- `clear(board, idx, jdx)`: removes a queen from the square at the given row and column indices on the input chessboard

### Queen Functions
- `isSafe(board, row, col)`: returns true if it is safe to place a queen on the given row and column indices on the input chessboard
- `checkForValidSquares(board)`: returns true if there is at least one valid square where a queen can be placed
- `getLeastSafeCol(board)`: returns the column with the least number of safe squares on the input chessboard

### Solving Functions
- `check(board, col)`: recursively places queens on the input chessboard starting from the given column index, and returns true if a solution is found
- `solve(board)`: solves the n-queens problem on the input chessboard, and prints the solved chessboard if a solution is found
### Obtain Problem Specifics
- `getBoardFromKeyboard()`: prompts the user to input the size of the chessboard and the coordinates of any blocked squares, and returns the generated chessboard with blocked squares
- `getBoardHardCoded()`: returns a hard-coded chessboard with a size of 4 and three blocked squares

## Build
You can run the script in a Python environment and call 'solve(board)' directly.
