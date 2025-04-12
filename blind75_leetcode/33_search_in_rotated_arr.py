class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # target in left half
                else:
                    left = mid + 1  # target in right half
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1  # target in right half
                else:
                    right = mid - 1  # target in left half

        return -1


obj = Solution()
numbers = [4, 5, 6, 7, 0, 1, 2]
index_found = obj.search(numbers, target=0)
print(index_found)

# Time Complexity: O(log n) – Modified binary search.
# Space Complexity: O(1) – Constant space.
# 🔥 Commonly asked at Facebook, Google, and Amazon.
