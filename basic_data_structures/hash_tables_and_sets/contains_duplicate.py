def contains_duplicate(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:  # O(1) lookup
            return True
        seen.add(num)  # O(1) insertion
    return False

if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    res = contains_duplicate(nums)
    print('true' if res else 'false')