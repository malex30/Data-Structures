class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # for loop iteration through a given nums List.
        # I start with the second iteration nums[1] range(1,...)
        # so that
        # the first iteration stays the same and I just change the
        # existing nums list
        for int in range(1, len(nums)):
            nums[int] += nums[int-1]
        return nums


# time complexity o(n) because I interate through each index
# space complexity o(1) because no new data structure is proportionally created