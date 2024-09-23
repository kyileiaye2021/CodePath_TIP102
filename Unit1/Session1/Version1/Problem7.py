#Unit 1 
#Session 1
#Version 1
#Problem 7

def good_pairs(pile1, pile2, k):
  # using count var to trace the total num of divisible ele
  count = 0

  # iterate over pile1
  for i in range(len(pile1)):

    # iterate over pile2
    for j in range(len(pile2)):

      # check if the pile2 ele * k divides pile1 ele
      if pile1[i] % (pile2[j] * k) == 0:
        count += 1

  return count
  
pile1 = [1, 3, 4]
pile2 = [1, 3, 4]
k = 1
print(good_pairs(pile1, pile2, k))

pile1 = [1, 2, 4, 12]
pile2 = [2, 4]
k = 3
print(good_pairs(pile1, pile2, k))


pile1 = [1, 3, 4]
pile2 = [1, 3, 4]
k = 1
good_pairs(pile1, pile2, k)

pile1 = [1, 2, 4, 12]
pile2 = [2, 4]
k = 3
good_pairs(pile1, pile2, k)