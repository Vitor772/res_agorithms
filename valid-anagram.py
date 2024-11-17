from itertools import count


def is_anagram(s: str, t: str) -> bool:

    if len(s) != len(t):
        return False

    count_s = {}
    count_t = {}

    for char in s:
        count_s[char] = count_s.get(char, 0) + 1
    for char in t:
        count_t[char] = count_t.get(char, 0) + 1

    return count_s == count_t

s = "anagram"
t = "nagaram"
print(is_anagram(s, t))

s = "rat"
t = "car"
print(is_anagram(s, t))
