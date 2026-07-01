class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_search = {}
        for i, num in enumerate(nums):
             if target - num in idx_search:
                return [i, idx_search[target - num]]
             idx_search[num] = i




        


        