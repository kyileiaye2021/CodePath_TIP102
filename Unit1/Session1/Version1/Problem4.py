#unit 1
# session 1
# ver 1
# problem 4

def non_decreasing(nums):
  replaced = False
  for i in range(1, len(nums)):
    if nums[i] < nums[i-1] and replaced:
      return False
    elif nums[i] < nums[i-1]:
      replaced = True

  return True

nums = [4, 2, 3]
print(non_decreasing(nums))

nums = [4, 2, 1]
print(non_decreasing(nums))


