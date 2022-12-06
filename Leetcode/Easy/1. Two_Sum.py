# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """Given an array of integers nums and an integer target, 
            return indices of the two numbers such that they add up to target.

        Args:
            nums (list[int]): A list of integers
            target (int): The given target number

        Returns:
            list[int]: The indices of two numbers in the list
        """
        # **********************************************
        # Key question: how to check all the combination of the two numbers
        # **********************************************
        for i in range(len(nums)):
            for j in range(len(nums)): 
                if nums[i]+nums[j] == target and i!=j:
                    return [i,j]


    

sol = Solution()
print(sol.twoSum([3,3],6))