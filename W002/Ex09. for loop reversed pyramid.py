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
reversespell('phone')