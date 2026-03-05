def remove_vowels(s: str) -> str:
    vowels = "aeiouAEIOU"
    result = ""
    for char in s:
        if char not in vowels:
            result += char
    return result

if __name__ == "__main__":
    s = input()
    res = remove_vowels(s)
    print(res)