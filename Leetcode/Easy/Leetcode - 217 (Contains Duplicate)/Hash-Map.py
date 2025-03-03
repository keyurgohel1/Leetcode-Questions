class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d1 = {}
        for i in range(len(nums)):
            if nums[i] in d1:
                d1[nums[i]] += 1
            else:
                d1[nums[i]] = 1
        for val in d1.values():
            if val > 1:
                return True
        return False