class Solution:

  def threeSum(self, nums: List[int]) -> List[List[int]]:
    # output array
    out: list = []

    # sort the array
    nums.sort()

    # iterate through the array
    for i, num in enumerate(nums):
      # skip duplicates for the first element
      if i > 0 and num == nums[i - 1]:
        continue

      # keep track of pointers for the remaining two numbers
      left: int = i + 1
      right: int = len(nums) - 1

      # looping through using two pointers
      while left < right:
        # calculate the current sum
        threeSum: int = num + nums[left] + nums[right]

        # threeSum is too big, move right pointer inward
        if threeSum > 0:
          right -= 1

        # threeSum is too small, move left pointer inward
        elif threeSum < 0:
          left += 1

        # found a valid triplet
        else:
          out.append([num, nums[left], nums[right]])

          # move pointers inward and skip duplicates for left and right
          left += 1
          right -= 1

          while left < right and nums[left] == nums[left - 1]:
            left += 1
          while left < right and nums[right] == nums[right + 1]:
            right -= 1

    return out