def RAM(sentence):
    UPPER=sentence.upper()
    split=UPPER.split()
    sum=' '
    for i in split:
        sum=sum+i[0]
    return sum

a=RAM('central processing unit')
print(a)