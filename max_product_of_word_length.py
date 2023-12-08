def max_product_of_word_length(words):
    max_product = 0
    product = 0
    first_word = words[0]

    for st in first_word:
        for nt in words[1:]:
            #import pdb;pdb.set_trace()
            if st not in nt and len(first_word) == len(nt):
                second_word = nt
        product = len(first_word) * len(second_word)
        first_word = nt
    if max_product < product:
        max_product = product
    return max_product



words = ["abcw","baz","foo","bar","xtfn","abcdef"]
print(max_product_of_word_length(words))
words_2 = ["a","ab","abc","d","cd","bcd","abcd"]
print(max_product_of_word_length(words_2))



