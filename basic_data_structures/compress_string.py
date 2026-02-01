def compress_string(s: str) -> str:
    if not s:
        return ""

    result = []
    current_char = s[0]
    count = 1

    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(current_char + str(count))
            current_char = s[i]
            count = 1
    result.append(current_char + str(count))

    return "".join(result)

if __name__ == "__main__":
    s = input()
    res = compress_string(s)
    print(res)
