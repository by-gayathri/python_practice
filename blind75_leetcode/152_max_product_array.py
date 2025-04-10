class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = max(nums)
        curr_max, curr_min = 1, 1

        for n in nums:
            if n == 0:
                curr_max, curr_min = 1, 1
                continue
            temp = n * curr_max
            curr_max = max(temp, n * curr_min, n)
            curr_min = min(temp, n * curr_min, n)
            result = max(curr_max, result)
        return result


obj = Solution()
numbers = [2, 3, -2, 4, 8]
maximum_product = obj.maxProduct(numbers)
print(maximum_product)

# Time Complexity: O(n) – Single pass through the array.
# Space Complexity: O(1) – Constant space used for tracking max/min
# 🚀 Interview favorite at Microsoft, Google, and Adobe.
