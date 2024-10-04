from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        result = []
        for n in nums:
            sum += n
            result.append(sum)
        return result
    


solution = Solution()

result = solution.runningSum([3,1,2,10,1])
print(result)