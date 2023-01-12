class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        sumNums = []
        # enumerate give me the index with the values
        for idx, elem in enumerate(nums):
            # starting the same array from the second index
            for idx2, elem2 in enumerate(nums[1:],1):
                print(idx2)
                Total = elem + elem2
                # if Total is equal to Target and indexes don't match: append to new array and return
                if Total == target and idx != idx2:
                    sumNums.append(idx)
                    sumNums.append(idx2)
                    return sumNums
                else:
                    continue

# time complexity o(nlog) because I interate through array twice
# space complexity o(1) because no new data structure is proportionally created