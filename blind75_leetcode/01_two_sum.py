class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in index_map:
                return [index_map[complement], i]
            index_map[num] = i
        return []


obj = Solution()
input_list = [20, 2, 0, 11, 15, 7]
target_sum = 9
index_list = obj.twoSum(input_list, target_sum)
print(f"Indices that make up to {target_sum} are {index_list}")

# Time Complexity: O(n) – We traverse the list once.
# Space Complexity: O(n) – In the worst case, we store all n elements in the dictionary.
