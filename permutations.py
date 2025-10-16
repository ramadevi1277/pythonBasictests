def permute(string, prefix=""):
    if len(string) == 0:
        print(prefix)
    else:
        for i in range(len(string)):
            import pdb;pdb.set_trace()
            rem = string[:i] + string[i+1:]
            permute(rem, prefix + string[i])

# Example usage
s = "ABC"
print(f"All permutations of '{s}':")
permute(s)