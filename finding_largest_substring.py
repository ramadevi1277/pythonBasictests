def logestSubstring(strs):
    substring = ""
    result_string = ""
    for each in strs:
        #import pdb;pdb.set_trace()
        if each not in substring:
            substring += each
        else:
            if len(result_string) <= len(substring):
                result_string = substring
                substring = ""
                substring += each
    return result_string


strs = "pwwkew"
strs_1 = "abcabcbb"
strs_2 = "bbbbb"
print(logestSubstring(strs))
print(logestSubstring(strs_1))
print(logestSubstring(strs_2))
