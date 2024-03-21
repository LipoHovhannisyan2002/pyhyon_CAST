s = "Hello world   "


def lengthOfLastWord(a):
    result = False
    splited_sent = s.split()
    i = len(splited_sent)

    for item in range(i-1,-1,-1):


        if splited_sent[item] and (65 <= ord(splited_sent[item][-1]) <= 90) or (97 <= ord(splited_sent[item][-1]) <= 122):

            result = True
            break
        x = i -1

    if result:
        return len(splited_sent[item])

print(lengthOfLastWord(s))
