SIZE = 9
#sudoku problem
#cells with value 0 are vacant cells
matrix = [
    [6,5,0,8,7,3,0,9,0],
    [0,0,3,2,5,0,0,0,8],
    [9,8,0,1,0,4,3,5,7],
    [1,0,5,0,0,0,0,0,0],
    [4,0,0,0,0,0,0,0,2],
    [0,0,0,0,0,0,5,0,3],
    [5,7,8,3,0,1,0,2,6],
    [2,0,0,0,4,8,9,0,0],
    [0,9,0,6,2,5,0,8,1]]

#step:1: find the total number of empty cells
def print_sudoku():
  for i in range(SIZE):
    print(matrix[i])

print_sudoku()

def number_unassigned(row, col):
    num_unassign = 0
    for i in range(0,SIZE):
        for j in range (0,SIZE):
            #cell is unassigned
            if matrix[i][j] == 0:
                row = i
                col = j
                num_unassign = 1
                a = [row, col, num_unassign]
                return a
    a = [-1, -1, num_unassign]
    return a

#unassigned_cells(0,0)
def isValid(r,c,val):
  for i in range(SIZE): 
    if matrix[r][i] == val:
      return False
  for i in range(SIZE): 
    if matrix[i][c] == val:
      return False 
  row_start = (r//3)*3
  col_start = (c//3)*3;
  #checking submatrix
  for i in range(row_start,row_start+3):
      for j in range(col_start,col_start+3):
          if matrix[i][j]==val:
              return False
  return True


def solve_sudoku():
  row = 0
  col = 0
  a = unassigned_cells(row,col)    

  if a[2] == 0:
    print('Sudoku is solved')
    return True

  r,c = a[0], a[1]  
  for i in range(1,10):
    if isValid(r,c,i):
      matrix[r][c] = i

      if solve_sudoku(): 
        return True
      matrix[r][c] = 0
  return False


if solve_sudoku():
    print_sudoku()
else:
    print("No solution")

def solve_sudoku():
    row = 0
    col = 0
    #if all cells are assigned then the sudoku is already solved
    #pass by reference because number_unassigned will change the values of row and col
    a = number_unassigned(row, col)
    if a[2] == 0:
        return True
    row = a[0]
    col = a[1]
    #number between 1 to 9
    for i in range(1,10):
        #if we can assign i to the cell or not
        #the cell is matrix[row][col]
        if is_safe(i, row, col):
            matrix[row][col] = i
            #backtracking
            if solve_sudoku():
                return True
            #f we can't proceed with this solution
            #reassign the cell
            matrix[row][col]=0
    return False    