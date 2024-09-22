#unit 1
#session 1
# ver 1
#prob 5

def find_missing_clues(clues, lower, upper):
  
  res_lst = []
  
  for i in range(len(clues)):
    
    if i == 0:
      if clues[i] != lower:
        res_lst.append([lower, clues[i] - 1])

    elif i == len(clues) - 1:
      if clues[i] != upper:
        res_lst.append([clues[i] + 1, upper])

    else:
      if clues[i] - clues[i - 1] > 1:
        res_lst.append([clues[i - 1] + 1, clues[i] - 1])

  return res_lst
      

clues = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(find_missing_clues(clues, lower, upper))

clues = [-1]
lower = -1
upper = -1
print(find_missing_clues(clues, lower, upper))

