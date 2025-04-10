class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [1] * n

        # Step 1: Prefix products
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Step 2: Suffix products (right to left)
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer


obj = Solution()
price_list = [1, 2, 3, 4]
product_array = obj.productExceptSelf(price_list)
print(product_array)

# Time Complexity: O(n) – Two linear passes.
# Space Complexity: O(1) extra space (excluding output array), since we’re not using extra arrays for prefix/suffix.
# 🚀 This problem is often asked at Google, Amazon, and Facebook.
