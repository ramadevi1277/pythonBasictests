sentence = "India is my country. My country is India."
split_sentance = sentence.lower().replace(".", "").split()
print(split_sentance)

for each in set(split_sentance):
    print("Count:%s %d" %(each, split_sentance.count(each)))