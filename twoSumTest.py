class Solution(object):
    def twoSum(self, nums, target):
        # Create a dictionary to store the elements and their indices
        num_dict = {}
        
        # Iterate through the list
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach the target
            complement = target - num
            
            # Check if the complement exists in the dictionary
            if complement in num_dict:
                # If yes, return the indices of the current number and its complement
                return [num_dict[complement], i]
            
            # If the complement doesn't exist, store the current number and its index in the dictionary
            num_dict[num] = i
            
        # If no solution is found, return an empty list
        return []