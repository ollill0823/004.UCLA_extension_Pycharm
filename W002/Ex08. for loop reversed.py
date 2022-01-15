### write a function that spells a given  word backwards.
# print word in reversed way (spelling)
def reversespell(word):
    for i in reversed (range(len(word))):
        print(word[i])
reversespell('phone')