#unit 1
#session 1
#ver 2
#prob 2

# happy case
# input: n = 3
# output: ["1", "2", "Hulk"]

# edge case
# input: n = 1
# output: ["1"]
# input: n = 2
# output: ["1", "2"]

def hulk_smash(n):
  res_lst = []
  i = 1
  while i <= n:
    if i % 3 == 0 and i % 5 == 0:
      res_lst.append("HulkSmash")
    elif i % 3 == 0:
      res_lst.append("Hulk")
    elif i % 5 == 0:
      res_lst.append("Smash")
    else:
      res_lst.append(f"{i}")
    i += 1
  return res_lst

n = 3
print(hulk_smash(n))

n = 5
print(hulk_smash(n))

n = 15
print(hulk_smash(n))
