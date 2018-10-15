class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return [0]
        cache_set = dict()
        for i, x in enumerate(nums):
            if (target - x) in cache_set:
                return [cache_set[target - x], i]
            cache_set[x] = i
        return [0]

result = Solution().twoSum([2, 7, 11, 15], 9)
print(result)