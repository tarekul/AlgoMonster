def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    return sorted(s) == sorted(t)

if __name__ == "__main__":
    s = input()
    t = input()
    res = is_anagram(s, t)
    print("true" if res else "false")