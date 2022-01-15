''''
   ## print as below
e
en
eno
enoh
enohp
'''
def reversespell(word):
    reverseword = '' # given a blank subset, then can add new word
    for i in reversed(range(len(word))):
         reverseword = reverseword + word[i]
         print (reverseword)
    return reverseword    # 若不return 回去以後,則不會print  最外層的reversespell('phone)

print(reversespell('phone'))  # 只能放最下面