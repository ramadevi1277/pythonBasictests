def removeStars(s):
    ans =[]
    for c in s:
        if c == '*':
            ans.pop()
        else:
            ans.append(c)

    print("".join(ans))

removeStars("leet**cod*d")

