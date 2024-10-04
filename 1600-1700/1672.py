from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(arr) for arr in accounts])  
    

print(Solution().maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))
    