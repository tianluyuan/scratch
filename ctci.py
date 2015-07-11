def permute_string(string):
    """ Returns a list of all possible permutations of string
    """
    if len(string) == 1:
        return [string]

    permuted = []
    used_chars = []
    for idx, char in enumerate(string):
        # skip if dupe
        if char in used_chars:
            continue
        used_chars.append(char)
        
        substring = string[0:idx]+string[idx+1:]
        for permuted_substring in permute_string(substring):
            permuted.append(char+permuted_substring)

    return permuted
