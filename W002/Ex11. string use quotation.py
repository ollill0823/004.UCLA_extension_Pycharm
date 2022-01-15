funstring1="I'm going to go to the gym. "
funstring2= "i\'m going to go to the gym. "
funstring3 = 'call ME Plz'
print(funstring1 == funstring2)
print('-------------------')
print('Capitalize : ', funstring3.capitalize())  # 設成只有第一個字母會大寫
secretcode= str.maketrans('abcdef', 'uvwzyz')   # a->u, b->v, c->w, d->z, e->y, f->z
secretstring =funstring3.translate(secretcode)  # translate funstring3 to my setting
stringcount = funstring3.count('call') # check how many word does the sentence has?
stringreplace = funstring3.replace('call','tell')
stringlower = funstring3.lower()
stringupper = funstring3.upper()

print('origin : ', funstring3)
print('translate : ', secretstring)
print('count : ', stringcount)
print('replace : ', stringreplace)
print('lower : ', stringlower)
print('upper : ', stringupper)