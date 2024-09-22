#unit 1
#session 1
# ver 1
# prob 3

def tiggerfy(word):
  word = word.lower()
  word = word.replace('t', '')
  word = word.replace('i', '')
  word = word.replace('gg', '')
  word = word.replace('er', '')
  return word
  
word = "Trigger"
print(tiggerfy(word))

word = "eggplant"
print(tiggerfy(word))

word = "Choir"
print(tiggerfy(word))