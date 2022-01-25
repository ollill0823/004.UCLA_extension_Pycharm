word=input('Enter a word: ')

def front_back(str):
  if len(str)<=1:
    return str
  else:
    front=str[:1]
    middle=str[1:-1]
    back = str[-1:]
    return back +  middle + front

z=front_back(word)
print(z)