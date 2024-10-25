def two_sum(nums, target):
    value_to_index = {val: idx for idx, val in enumerate(nums)}
    for num in nums:
        complement = target - num
        if complement in value_to_index and value_to_index[complement] != nums.index(num):
            return [nums.index(num), value_to_index[complement]]
    return []

print(two_sum([2, 7, 11, 15], 9))
