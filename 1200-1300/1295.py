from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return [x for x in nums if (len(str(x)) & 1) == 1]
    
print(Solution().findNumbers([12, 345, 2, 6, 7896]))        