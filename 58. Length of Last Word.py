def split_string(input_string, delimiter):
    substrings = []
    start_index = 0

    for i, char in enumerate(input_string):
        if char == delimiter:
            substring = input_string[start_index:i]
            substrings.append(substring)
            start_index = i + 1

    last_substring = input_string[start_index:]
    substrings.append(last_substring)

    return substrings

def lengthOfLastWord(input_string):
    delimiter = " "
    splited_sent = split_string(input_string.strip(), delimiter)
    i = len(splited_sent)

    for item in range(i - 1, -1, -1):
        if splited_sent[item] and (65 <= ord(splited_sent[item][-1]) <= 90) or (
                97 <= ord(splited_sent[item][-1]) <= 122):
            return len(splited_sent[item])

    return 0  


s = "H ello World! This is a sample string "
print(lengthOfLastWord(s))
