def lengthOfLastWord(input_string):
    length = len(input_string)
    last_word_length = 0
    last_word_found = False


    for i in range(length - 1, -1, -1):
        if input_string[i] != ' ':
            last_word_length += 1
            last_word_found = True



        elif last_word_found:
            break




    return last_word_length

s = "Hello World This "
print(lengthOfLastWord(s))
