class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


obj = Solution()
price_list = [1, 2, 3, 1]
is_duplicate = obj.containsDuplicate(price_list)
print(f"is the list contains duplicate elements?: {is_duplicate}")

# Time Complexity: O(n) – Each element is checked once.
# Space Complexity: O(n) – In the worst case, all n elements are stored in a set.
