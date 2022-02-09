def frequency(itemlist):
       num={}
       for i in itemlist:
              if i in num:
                     num[i] +=1
              else: num[i] =1
       return num

students = ['Cindy', 'John', 'Cindy', 'Adam', 'Adam', 'Jimmy', 'John', 'Cindy', 'John']
a=frequency(students)
print(a)