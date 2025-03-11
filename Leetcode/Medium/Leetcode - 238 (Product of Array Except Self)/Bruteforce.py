class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if j != i:
                    product = product * nums[j]
            answer.append(product)
        return answer
# Time Complexity: O(n^2)
# Space Complexity: O(n)
