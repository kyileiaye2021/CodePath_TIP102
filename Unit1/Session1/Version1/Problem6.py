#Unit 1
#Session 1
# Ver 1
# Problem 6

def harvest(vegetable_patch):
  count = 0
  m = len(vegetable_patch) # num of rows
  n = len(vegetable_patch[0]) # num of columns
  
  for i in range(m):
    for j in range(n):
      if vegetable_patch[i][j] == 'c':
        count += 1
        
  return count
        
vegetable_patch = [
  ['x', 'c', 'x'],
  ['x', 'x', 'x'],
  ['x', 'c', 'c'],
  ['c', 'c', 'c']
]
print(harvest(vegetable_patch))