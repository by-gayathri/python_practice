class Solution(object):
    def maxSubArray(self, nums):
        max_sum = nums[0]
        curr_sum = 0

        for num in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += num
            max_sum = max(max_sum, curr_sum)

        return max_sum


obj = Solution()
numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maximum_sum = obj.maxSubArray(numbers)
print(maximum_sum)

# Time Complexity: O(n) – Single pass through the array.
# Space Complexity: O(1) – Uses constant extra space.
# 🚀This is a super common question in interviews at Amazon, Bloomberg, and LinkedIn.
