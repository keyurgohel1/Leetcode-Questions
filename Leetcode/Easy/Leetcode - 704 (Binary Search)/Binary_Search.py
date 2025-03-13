class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            num = (left + right) // 2
            if nums[num] == target:
                return num
            if nums[num] < target:
                left = num + 1
            else:
                right = num - 1
        return -1
# Time Complexity: O(log n)
# Space Complexity: O(1)