class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num  # Move os elementos desejados para o início
                i += 1
        return i
