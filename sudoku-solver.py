"""
sudoku.py
Program to solve a 9x9 sudoku puzzle
Viennie Lee
August 2020
"""
import numpy as np
import time

def isValid(board, i, j, evalNum):
  # check row
  for b in range(0,8):
    if board[i][b] == evalNum:
      return False
  # check col
  for a in range(0,8):
    if board[a][j] == evalNum:
      return False
  # set box index range
  boxLeft = i - i%3
  boxTop = j - j%3
  # TODO check these since had to change range
  for c in range(boxLeft, boxLeft + 3):
    for d in range(boxTop, boxTop + 3):
      if c==i and d==j:
        continue
      if board[c][d] == evalNum:
        return False
  return True

def getNextValid(board, i, j):
  if board[i][j] == 9:
    return 0
  for nextNum in range(int(board[i][j] + 1), 10):
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
  board_in2 = np.array([
          [0,5,0,0,4,0,0,0,9],
          [0,1,0,6,0,0,5,4,0],
          [0,3,0,0,5,7,8,0,0],
          [3,6,0,0,0,9,0,0,0],
          [4,0,8,5,0,3,1,0,2],
          [0,0,0,7,0,0,0,6,8],
          [0,0,3,2,9,0,0,8,0],
          [0,8,1,0,0,6,0,2,0],
          [5,0,0,0,8,0,0,7,0]
  ])
  whole_solution = np.add(board_in,solution)
  solutions_board = np.zeros(shape=(9,9), dtype = int)
  combined_board = board_in
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
          # cut branch back to latest parent
          b = branch_spot[-1][1]
          if b == 8:
              b = 0
          else:
            b+=1
          for a in range(branch_spot[-1][0], i+1) :
            if branch_spot[-1][1] == 8:
              a+=1
            while b <= 8:
              solutions_board[a][b] = 0
              b += 1
            b = 0
            
          # update cell index to start over at latest branch
          i = branch_spot[-1][0]
          j = branch_spot[-1][1]
          update_branchSpot(np.add(board_in,solutions_board), i, j, branch_spot)
        else:
        # valid number, fill as usual
          solutions_board[i][j] = getNextValid(np.add(board_in,solutions_board), i, j)
          # TODO COMBINED BOARD DOESNT HAVE THE UPDATE SO IT ERRORS
          update_branchSpot(np.add(board_in,solutions_board), i, j, branch_spot)
          j+=1
      else:
      # number given
        j+=1
      combined_board = np.add(board_in,solutions_board)
      
    i+=1
    j=0
  elapsed_time = time.process_time() - t
  print("Elapsed time: %f seconds" % elapsed_time)
  print(*solutions_board)

if __name__ == "__main__":
    main()
