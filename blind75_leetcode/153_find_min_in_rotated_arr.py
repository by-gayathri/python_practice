class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


obj = Solution()
numbers = [5, 1, 2, 3, 4]
min_number = obj.findMin(numbers)
print(min_number)

# Time Complexity: O(log n) – Binary search.
# Space Complexity: O(1) – Constant space.
# 🎯 This is a favorite at Google, Uber, and Apple.
