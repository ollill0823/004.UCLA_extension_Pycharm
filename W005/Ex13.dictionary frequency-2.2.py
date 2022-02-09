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
       if a[j]==1:
              print('{:<9} appears {} time.'.format(j, a[j]))
       else:
              print('{:<9} appears {} times.'.format(j, a[j]))