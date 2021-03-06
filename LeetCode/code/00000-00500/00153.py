from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        while i < j:
            mid = i + (j - i) // 2
            if nums[mid] > nums[j]:
                i = mid + 1
            elif nums[mid] < nums[j]:
                j = mid
            else:
                break
        return nums[i]