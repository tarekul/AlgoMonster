def sort_list(unsorted_list: list[int]) -> list[int]:
    for i in range(1, len(unsorted_list)):
        key = unsorted_list[i]
        j = i - 1
        while j >=0 and unsorted_list[j] > key:
            unsorted_list[j + 1] = unsorted_list[j]
            j -= 1
        unsorted_list[j + 1] = key
    return unsorted_list

if __name__ == "__main__":
    unsorted_list = [int(x) for x in input().split()]
    res = sort_list(unsorted_list)
    print(" ".join(map(str, res)))
