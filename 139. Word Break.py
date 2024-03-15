s = "leetcode"
wordDict = ["leet","code"]


wordset = set(wordDict)
n = len(s)
dp = [False] * (n+1)
dp[0] = True
for i in range(1,n+1):
    for j in range(i):
        if dp[j] and s[j:i] in wordset:
            dp[i] = True
            break
print(dp[n])