def count_frequencies(arr: list[int]) -> dict[int, int]:
    freq = {}
    
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    return freq

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    res = count_frequencies(arr)
    for key in sorted(res.keys()):
        print(key, res[key])