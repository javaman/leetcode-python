
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currentCount = 0
        result = 0
        for n in nums:
            if n == 1:
                currentCount += 1
            else:
                result = max([currentCount, result])
                currentCount = 0
        return max([currentCount, result])
        