class Solution:
    def sortEvenOdd(self, nums: list[int]) -> list[int]:
        a = []
        b = []
        n = len(nums)
        for i in range(n):
            if i % 2 == 0:
                a.append(nums[i])
            else:
                b.append(nums[i])
        a.sort(reverse = True)
        b.sort()
        for i in range(n):
            if i % 2 == 0:
                nums[i] = a.pop()
            else :
                nums[i] = b.pop()
        return nums
            
            