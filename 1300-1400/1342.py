class Solution:
    def numberOfSteps(self, num: int) -> int:
        result = 0
        while num > 0:
            result = result + 1
            if num % 2 == 0:
                num = num / 2
            else:
                num = num - 1
        return result
        

print(Solution().numberOfSteps(123))