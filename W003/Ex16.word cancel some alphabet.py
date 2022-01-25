word=input('Enter a word: ')


def string_bits(str):
  result = ''
  for i in range(0,len(str),2):
      result = result + str[i]
  return result


z=string_bits(word)
print(z)
