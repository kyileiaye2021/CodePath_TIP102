#unit 1
#session 1
#ver 2
#prob 1

# happy cases
# input: words = ["batman", "superman"], x = 'a'
# output: [0,1]

# edge cases
# input: words = ['hulk', 'abs'], x = 'e'
# output: []

# create a res_list
# iterate over the list
#   check if x is in the curr word
#     append the curr index in the res_lst
# return res_lst

def words_with_char(words, x):
  res_lst = []
  for i in range(len(words)):
    if x in words[i]:
      res_lst.append(i)

  return res_lst

words = ["batman", "superman"]
x = "a"
print(words_with_char(words, x))

words = ["black panther", "hulk", "black widow", "thor"]
x = "a"
print(words_with_char(words, x))

words = ["star-lord", "gamora", "groot", "rocket"]
x = "z"
print(words_with_char(words, x))