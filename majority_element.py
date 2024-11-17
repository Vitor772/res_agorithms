def majority_element(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else - 1)

    if nums.count(candidate) > len(nums) // 2:
        return candidate
    return None

nums = [3, 2, 3]
print(majority_element(nums))