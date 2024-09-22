#unit 1
#session 1
# version 1
#prob 2

def final_value_after_operations(operations):
  trigger = 1
  for ele in operations:
    if ele == "bouncy" or ele == "flouncy":
      trigger += 1
    elif ele == "trouncy" or ele == "pouncy":
      trigger -= 1

  return trigger

operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations))

operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations))
