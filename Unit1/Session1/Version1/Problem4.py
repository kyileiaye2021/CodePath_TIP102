#unit 1
# session 1
# ver 1
# problem 4

def non_decreasing(nums):
  for i in range(1, len(nums)):
    if nums[i] < nums[i-1]:
      return False

  return True

nums = [1, 2, 3]
print(non_decreasing(nums))

nums = [4, 2, 1]
print(non_decreasing(nums))


