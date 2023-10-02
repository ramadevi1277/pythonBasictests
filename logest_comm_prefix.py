strs = ["flower", "flow", "flight"]

def longestCommonPrefix(strs):
    l = len(strs[0])
    for i in range(1, len(strs)):
        #import pdb;pdb.set_trace()
        length = min(l, len(strs[i]))
        while length > 0 and strs[0][0:length] != strs[i][0:length]:
            length = length - 1
            if length == 0:
                return 0
    return strs[0][0:length]

print(longestCommonPrefix(strs))
