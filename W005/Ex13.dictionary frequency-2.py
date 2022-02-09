def wordcount(list):
       split=list.split()
       count={}
       for i in split:
              if i in count:
                     count[i] +=1
              else:
                     count[i] =1
       return count

text=input('Enter something: ')
a=wordcount(text)

for j in a:
       print('{:<9} '.format(j), end='')
       if a[j]>1:
              print('appears', a[j] ,'times'  )
       else:
              print('appears', a[j] ,'time'  )