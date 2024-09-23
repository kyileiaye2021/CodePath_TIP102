#unit 1
#session 1
#ver 1
#prob 8

def local_maximums(grid):
  rows = len(grid)
  cols = len(grid[0])
  res_lst = []

  for i in range(1, rows - 1):
    row = []
    for j in range(1, cols - 1):
      max_val = max(grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1],
                   grid[i][j-1], grid[i][j], grid[i][j+1],
                   grid[i+1][j-1], grid[i+1][j], grid[i+1][j+1])

      row.append(max_val)

    res_lst.append(row)

  return res_lst

grid = [
  [9, 9, 8, 1],
  [5, 6, 2, 6],
  [8, 2, 6, 4],
  [6, 2, 2, 2]
]
print(local_maximums(grid))

grid = [
  [1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1],
  [1, 1, 2, 1, 1],
  [1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1]
]
print(local_maximums(grid))

grid = [    
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
print(local_maximums(grid))

grid = [    
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
print(local_maximums(grid))