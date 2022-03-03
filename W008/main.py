a=['3','4','5','6','7']
check =False

for i in a:
    print('i',i)
    if i == '4' :
        check = True
    elif check ==True :
        a.remove(i)
        check=False

print(a)

