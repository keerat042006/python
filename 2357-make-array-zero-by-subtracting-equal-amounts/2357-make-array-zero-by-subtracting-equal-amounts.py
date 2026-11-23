class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        b = []
        for i in nums:
            if i not in b and i != 0:
                b.append(i)
        return len(b)

        