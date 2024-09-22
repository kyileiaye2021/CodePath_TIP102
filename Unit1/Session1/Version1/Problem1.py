# Unit 1
# Session 1
# Version 1
# Problem 1

def linear_search(lst, target):
  found = False
  for i in range(len(lst)):
    if lst[i] == target:
      found = True
      print(i)
      break

  if not found:
    print(-1)
  

items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
linear_search(items, target)

items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
linear_search(items, target)