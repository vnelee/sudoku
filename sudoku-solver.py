"""
sudoku-solver.py
Program to solve a 9x9 sudoku puzzle
Viennie Lee
August 2020
"""
import numpy as np
import time

def isValid(board, i, j, evalNum):
  # check row
  if evalNum in board[i,:]:
    return False
  # check col
  if evalNum in board[:,j]:
    return False
  # check box
  boxLeft = i - i%3
  boxTop = j - j%3
  if evalNum in board[boxLeft:boxLeft+3, boxTop:boxTop+3]:
    return False
  return True

def getNextValid(board, i, j):
  if board[i][j] == 9:
    return 0
  for nextNum in range(board[i][j] + 1, 10):
    if isValid(board, i, j, nextNum):
      return nextNum
  return 0

def update_branchSpot(board, i, j, branch_spot):
  if getNextValid(board, i, j) != 0:
    if len(branch_spot) == 0 or (branch_spot[-1] != [i,j]):
      branch_spot.append([i,j])
      return
  elif getNextValid(board, i, j) == 0 and branch_spot[-1] == [i,j]:
    branch_spot.pop()
    return

def main():
  
  board_in = np.array([
          [8,0,0,0,0,0,0,0,0],
          [0,0,3,6,0,0,0,0,0],
          [0,7,0,0,9,0,2,0,0],
          [0,5,0,0,0,7,0,0,0],
          [0,0,0,0,4,5,7,0,0],
          [0,0,0,1,0,0,0,3,0],
          [0,0,1,0,0,0,0,6,8],
          [0,0,8,5,0,0,0,1,0],
          [0,9,0,0,0,0,4,0,0]
  ])
  solutions_board = np.zeros(shape=(9,9), dtype = int)
  branch_spot = []
  i = 0
  j = 0
  t = time.process_time()

  # going through each cell in order by row
  while i <= 8:
    while j <= 8:
      if board_in[i][j] == 0:
        if getNextValid(np.add(board_in,solutions_board), i, j) == 0:
          # dead end case - no more valid #'s  
          # cut back to latest child with branch
          b = branch_spot[-1][1]
          if b == 8:
              a = branch_spot[-1][0] + 1
              b = 0
          else:
            a = branch_spot[-1][0]
            b+=1
          for a in range(branch_spot[-1][0], i+1) :
            while b <= 8:
              solutions_board[a][b] = 0
              b += 1
            b = 0
          # update cell index to start over at latest branch
          i = branch_spot[-1][0]
          j = branch_spot[-1][1]
          update_branchSpot(np.add(board_in,solutions_board), i, j, branch_spot)
        else:
        # valid number
          solutions_board[i][j] = getNextValid(np.add(board_in,solutions_board), i, j)
          update_branchSpot(np.add(board_in,solutions_board), i, j, branch_spot)
          j+=1
      else:
      # number given
        j+=1
    i+=1
    j=0
  elapsed_time = time.process_time() - t
  print("Elapsed time: %f seconds" % elapsed_time)
  print(*solutions_board)

if __name__ == "__main__":
    main()
