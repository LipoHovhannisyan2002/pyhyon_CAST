s = "Hello World  "


def lengthOfLastWord( a):
    result = False
    splited = s.split()
    i = len(splited)
    for item in reversed(splited):
        if item and (65 <= ord(item[-1]) <= 90) or (97 <= ord(item[-1]) <= 122):
            result = True
            break
        i-=1
    if result:
        return len(item)

print(lengthOfLastWord(s))