def can_make_arithmetic_progression(arr: list[int]) -> bool:
    arr.sort()
    diff = arr[1] - arr[0]
    
    for i in range(2, len(arr)):
        if arr[i] - arr[i-1] != diff:
            return False
    
    return True

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    res = can_make_arithmetic_progression(arr)
    print("true" if res else "false")
