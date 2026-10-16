class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        count = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                twosum = nums[i]  + nums[j]
                if twosum == target:
                    return [i, j]