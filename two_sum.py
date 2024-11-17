def two_sum(target, nums):
    hasher = {}

    for idx, i in enumerate(nums):
        if i in hasher:
            return [hasher.get(i), idx]
        hasher[target - i] = idx

nums = [1, 2, 16, 17, 5, 5]
target = 10

resultado = two_sum(target, nums)
print(resultado)
