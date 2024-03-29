def length_of_longest_substring(s):
    start = 0
    end = 0
    max_length = 0
    seen = set()

    while end < len(s):
        if s[end] not in seen:
            seen.add(s[end])
            max_length = max(max_length, end - start + 1)
            end+=1
        else:
            seen.remove(s[start])
            start += 1

    return max_length

s = "abcabcbb"
print(length_of_longest_substring(s))
