""" Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order. 
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:
Input: nums = [3,3], target = 6
Output: [0,1] """

# Solution below:
def two_sum(nums, target):
    # Setting nums as list
    if nums is None:
        nums = []

    # Storing items in a dictionary
    output = {}
    # Loop through values in nums and enumerating with an index as (i)
    for i, value in enumerate(nums):
        # Subtracting target with value in nums
        result = target - value
        # Checking if the result is present in output.
        if result in output:
						# Gets the index of the matching pair and index of first number which is stored as the key.
            return [output[result], i] 
        else:
            output.update({value: i})

x = two_sum([2, 11, 15, 7], 9)
print(x)



